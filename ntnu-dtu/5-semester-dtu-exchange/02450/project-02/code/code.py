import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

from scipy import stats
from tabulate import tabulate
from ucimlrepo import fetch_ucirepo 
from sklearn.metrics import mean_squared_error
from sklearn import model_selection
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import Ridge, LinearRegression, LogisticRegression
from toolbox_02450 import rlr_validate
from mlxtend.evaluate import mcnemar_table, mcnemar
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from scipy.stats import ttest_rel

warnings.filterwarnings('ignore')

'''
02450 - Introduction to Machine Learning and Data Mining
Project 2 - 16.11.2023 - Technical University of Denmark

@authors
- Jørgen Finsveen
- Even J. P. Haslerud
'''




# Part 1a: Regression Analysis and Feature Selection
# ------------------------------------------------


    # Retrieving and processing dataset
    # --------------------------------

heart_disease = fetch_ucirepo(id=45) 
df = pd.concat([heart_disease.data.features, heart_disease.data.targets], axis=1)
df.dropna(inplace=True)

# One-of-K encoding for categorical variables
df = pd.get_dummies(df, drop_first=True)

# Removes rows with one or more NaN values
df.dropna(inplace=True)

# Separate the target variable 'thalach' and the features
X = df.drop('thalach', axis=1).values
y = df['thalach'].values

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

raw = df.values




    # Regression, Part a1)
    # --------------------------------



_variables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
plt.figure(figsize=(24,12))
r = 0; c = 1

# Plotting subplots of variable estimations
for i in range(len(_variables)):
    attr_col = list(df.columns).index(_variables[i])
    cols = list(range(0, attr_col)) + list(range(attr_col + 1, len(df.columns)))

    x = raw[:, cols]
    y = raw[:, attr_col]

    x = stats.zscore(x);

    model = lm.LinearRegression()
    model.fit(x,y)

    y_est = model.predict(x)
    residual = y_est-y

    r += 1
    if (r > 3):
        r = 1
        c += 1
    
    plt.subplot(2, 3, r + c * 3 - 3)
    plt.plot(y, y, '--r')
    plt.plot(y, y_est, '.g')
    plt.xlabel('Value of {0} (true)'.format(_variables[i])); plt.ylabel('Value of {0} variable (estimated)'.format(_variables[i]))
    plt.legend(['True values', 'Estimated values'], loc = 2)
    plt.grid()
plt.show()


# Plotting correlation heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()



    # Regression, Part a2)
    # --------------------------------



attr_col = list(df.columns).index('thalach')
cols = list(range(0, attr_col)) + list(range(attr_col + 1, len(df.columns)))

x = raw[:, cols]
y = raw[:, attr_col]
attribute_names = list(df.columns[cols])
N, M = x.shape


x = np.concatenate((np.ones((x.shape[0],1)),x),1)
attributeNames = [u'Offset'] + attribute_names
M = M+1


K = 10
CV = model_selection.KFold(K, shuffle=True)

lambdas = np.power(10.,range(-5,9))

Error_train = np.empty((K,1))
Error_test = np.empty((K,1))
Error_train_rlr = np.empty((K,1))
Error_test_rlr = np.empty((K,1))
Error_train_nofeatures = np.empty((K,1))
Error_test_nofeatures = np.empty((K,1))

val_error_lambdas = np.empty((K,len(lambdas)))
w_rlr = np.empty((M,K))
mu = np.empty((K, M-1))
sigma = np.empty((K, M-1))
w_noreg = np.empty((M,K))

k=0
for train_index, test_index in CV.split(X,y):
    
    X_train = x[train_index]
    y_train = y[train_index]
    X_test = x[test_index]
    y_test = y[test_index]
    internal_cross_validation = 10    
    
    opt_val_err, opt_lambda, mean_w_vs_lambda, train_err_vs_lambda, test_err_vs_lambda = rlr_validate(X_train, y_train, lambdas, internal_cross_validation)
    val_error_lambdas[k] = test_err_vs_lambda
    
    print("\nValidation error for optimal lambda in k={0}: {1}".format(k+1, opt_val_err))
    print("Optimal lambda selected in k={0}: {1}".format(k+1, opt_lambda))
    
    Xty = X_train.T @ y_train
    XtX = X_train.T @ X_train
    
    # Compute mean squared error
    Error_train_nofeatures[k] = np.square(y_train-y_train.mean()).sum(axis=0) / y_train.shape[0]
    Error_test_nofeatures[k] = np.square(y_test-y_test.mean()).sum(axis=0) / y_test.shape[0]
    

    # Estimate weights for the optimal value of lambda
    lambdaI = opt_lambda * np.eye(M)
    lambdaI[0,0] = 0 
    w_rlr[:,k] = np.linalg.solve(XtX+lambdaI,Xty).squeeze()

    # Compute mean squared error with regularization with optimal lambda
    Error_train_rlr[k] = np.square(y_train-X_train @ w_rlr[:,k]).sum(axis=0) / y_train.shape[0]
    Error_test_rlr[k] = np.square(y_test-X_test @ w_rlr[:,k]).sum(axis=0) / y_test.shape[0]

    # Estimate weights for unregularized linear regression
    w_noreg[:,k] = np.linalg.solve(XtX,Xty).squeeze()

    # Compute mean squared error without regularization
    Error_train[k] = np.square(y_train-X_train @ w_noreg[:,k]).sum(axis=0) / y_train.shape[0]
    Error_test[k] = np.square(y_test-X_test @ w_noreg[:,k]).sum(axis=0) / y_test.shape[0]

    if k == K-1:
        plt.figure(k, figsize=(12,8))
        plt.subplot(1,2,1)
        plt.semilogx(lambdas,mean_w_vs_lambda.T[:,1:],'.-') 
        plt.xlabel('Regularization factor')
        plt.ylabel('Mean Coefficient Values')
        plt.grid()
        
        plt.subplot(1,2,2)
        plt.title('Optimal lambda: 1e{0}'.format(np.log10(opt_lambda)))
        plt.loglog(lambdas,train_err_vs_lambda.T,'b.-', lambdas,test_err_vs_lambda.T,'r.-')
        plt.xlabel('Regularization factor')
        plt.ylabel('Squared error (crossvalidation)')
        plt.legend(['Train error', 'Validation error'])
        plt.grid()

    k+=1

plt.show()

# Displaying results
print('Linear regression without feature selection:')
print('- Training error: {0}'.format(Error_train.mean()))
print('- Test error:     {0}'.format(Error_test.mean()))
print('- R^2 train:     {0}'.format((Error_train_nofeatures.sum()-Error_train.sum())/Error_train_nofeatures.sum()))
print('- R^2 test:     {0}\n'.format((Error_test_nofeatures.sum()-Error_test.sum())/Error_test_nofeatures.sum()))

print('Regularized linear regression:')
print('- Training error: {0}'.format(Error_train_rlr.mean()))
print('- Test error:     {0}'.format(Error_test_rlr.mean()))
print('- R^2 train:     {0}'.format((Error_train_nofeatures.sum()-Error_train_rlr.sum())/Error_train_nofeatures.sum()))
print('- R^2 test:     {0}\n'.format((Error_test_nofeatures.sum()-Error_test_rlr.sum())/Error_test_nofeatures.sum()))

print('\n\nGeneralization error for different values of lambda:')

for i in range(len(lambdas)):
    print('{:>20} {:>20}'.format(float(lambdas[i]), str(np.round(val_error_lambdas.mean(axis = 0)[i],2))))




# Preparing the cross-validation
outer_cv = model_selection.KFold(n_splits=5, shuffle=True)   # 5 outer folds
inner_cv = model_selection.KFold(n_splits=10, shuffle=True)  # 10 inner folds

error_train_full_model = []
error_test_full_model = []
error_train_fs_model = []
error_test_fs_model = []
r2_train_full_model = []
r2_test_full_model = []
r2_train_fs_model = []
r2_test_fs_model = []

# Performing the cross-validation
for train_index, test_index in outer_cv.split(X_scaled):

    # Spliting data into training and test sets for CV fold
    X_train, X_test = X_scaled[train_index], X_scaled[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Fitting the model with no feature selection
    full_model = LinearRegression().fit(X_train, y_train)
    y_train_pred_full = full_model.predict(X_train)
    y_test_pred_full = full_model.predict(X_test)
    
    # Calculating errors for the model
    error_train_full_model.append(np.mean((y_train - y_train_pred_full) ** 2))
    error_test_full_model.append(np.mean((y_test - y_test_pred_full) ** 2))
    r2_train_full_model.append(full_model.score(X_train, y_train))
    r2_test_full_model.append(full_model.score(X_test, y_test))

    # Feature selection with forward selection
    sfs = SequentialFeatureSelector(full_model, n_features_to_select="auto", direction='forward', cv=inner_cv)
    sfs = sfs.fit(X_train, y_train)
    
    # Fitting the model with the selected features
    fs_model = LinearRegression().fit(X_train[:, sfs.get_support()], y_train)
    y_train_pred_fs = fs_model.predict(X_train[:, sfs.get_support()])
    y_test_pred_fs = fs_model.predict(X_test[:, sfs.get_support()])

    # Calculating the errors for the model
    error_train_fs_model.append(np.mean((y_train - y_train_pred_fs) ** 2))
    error_test_fs_model.append(np.mean((y_test - y_test_pred_fs) ** 2))
    r2_train_fs_model.append(fs_model.score(X_train[:, sfs.get_support()], y_train))
    r2_test_fs_model.append(fs_model.score(X_test[:, sfs.get_support()], y_test))

# Display results
print('\nFull model without feature selection:')
print(f'- Average training error: {np.mean(error_train_full_model)}')
print(f'- Average test error: {np.mean(error_test_full_model)}')
print(f'- Average R^2 train: {np.mean(r2_train_full_model)}')
print(f'- Average R^2 test: {np.mean(r2_test_full_model)}\n')

print('Model with feature selection:')
print(f'- Average training error: {np.mean(error_train_fs_model)}')
print(f'- Average test error: {np.mean(error_test_fs_model)}')
print(f'- Average R^2 train: {np.mean(r2_train_fs_model)}')
print(f'- Average R^2 test: {np.mean(r2_test_fs_model)}')


# Range of lambda values to test
lambdas = np.logspace(-5, 2, 100)  

# Preparing new cross-validation
cv = model_selection.KFold(n_splits=10, shuffle=True, random_state=42)

avg_generalization_error = []

# Performing a 10-fold cross-validation and calculating generalization error for each lambda
for lambda_ in lambdas:
    
    fold_errors = []
    
    for train_index, test_index in cv.split(X_scaled):
        
        X_train, X_test = X_scaled[train_index], X_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Creating Ridge regression model with the lambda
        model = Ridge(alpha=lambda_)

        # Fitting the model
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # Calculating the mean squared error for the fold
        mse = mean_squared_error(y_test, y_pred)
        fold_errors.append(mse)

    # Calculating the average generalization error
    avg_generalization_error.append(np.mean(fold_errors))

# Plotting the generalization error as a function of lambda
plt.figure(figsize=(10, 6))
plt.semilogx(lambdas, avg_generalization_error, label='Generalization Error')
plt.xlabel('Lambda')
plt.ylabel('Generalization Error')
plt.title('Generalization Error as a Function of Lambda')
plt.legend()
plt.show()

# Finding the lambda with the lowest generalization error
min_error = min(avg_generalization_error)
opt_lambda = lambdas[avg_generalization_error.index(min_error)]
print(f'The optimal lambda value is: {opt_lambda}')

# Fitting the ridge regression model with optimal lambda
optimal_ridge_model = Ridge(alpha=opt_lambda)
optimal_ridge_model.fit(X_scaled, y)

# Getting the weight coefficients and intercept
weights = optimal_ridge_model.coef_
intercept = optimal_ridge_model.intercept_

feature_names = df.drop('thalach', axis=1).columns
print("\n\nIntercept:", intercept)
print("Feature weights:")
for name, weight in zip(feature_names, weights):
    print(f"{name}: {weight}")






    # Regression, Part a3)
    # --------------------------------


optimal_ridge_model = Ridge(alpha=opt_lambda)
optimal_ridge_model.fit(X_scaled, y)

weights = optimal_ridge_model.coef_
intercept = optimal_ridge_model.intercept_

feature_names = df.drop('thalach', axis=1).columns
print("\nIntercept:", intercept)
print("Feature weights:")
for name, weight in zip(feature_names, weights):
    print(f"{name}: {weight}")

'''
x_new = [
    [62, 1, 1, 145, 242, 1, 2, 0, 2.3, 3, 0.0, 6.0, 0],
    [37, 1, 3, 125, 252, 0, 0, 0, 3.5, 3, 0.0, 3.0, 0]
]
y_predicted = optimal_ridge_model.predict(x_new)
print("\n\nPredicted output:", y_predicted)
'''

print("\nPerforming two-level cross validation...\n")

# CLASSIFICATION 1-5

lambda_values = np.logspace(-5, 2, 100)
h_values = [1, 2, 4, 8, 16, 32, 64]


# Initialize results dataframe
results_df = pd.DataFrame(columns=['Fold', 'Baseline Error', 'Optimal λ', 'Ridge Error', 'Optimal h', 'ANN Error'])

# Performing two-level cross-validation
for fold, (train_index, test_index) in enumerate(outer_cv.split(X_scaled), start=1):
    X_train, X_test = X_scaled[train_index], X_scaled[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Baseline model for mean predictor
    baseline_pred = np.full_like(y_test, y_train.mean())
    baseline_error = mean_squared_error(y_test, baseline_pred)

    
    best_lambda = None
    best_ridge_error = np.inf
    for lambda_ in lambda_values:
        
        ridge_errors = []
        for inner_train_index, inner_val_index in inner_cv.split(X_train):
            X_inner_train, X_inner_val = X_train[inner_train_index], X_train[inner_val_index]
            y_inner_train, y_inner_val = y_train[inner_train_index], y_train[inner_val_index]

            # Training Ridge model and calculate error
            ridge_model = Ridge(alpha=lambda_)
            ridge_model.fit(X_inner_train, y_inner_train)
            y_inner_pred = ridge_model.predict(X_inner_val)
            ridge_errors.append(mean_squared_error(y_inner_val, y_inner_pred))

        # Updating best lambda if current model is better
        avg_ridge_error = np.mean(ridge_errors)
        if avg_ridge_error < best_ridge_error:
            best_ridge_error = avg_ridge_error
            best_lambda = lambda_

    # Training final Ridge model with optimal lambda and calculate error
    final_ridge_model = Ridge(alpha=best_lambda).fit(X_train, y_train)
    ridge_error = mean_squared_error(y_test, final_ridge_model.predict(X_test))

    best_h = None
    best_ann_error = np.inf
    for h in h_values:
        
        ann_errors = []
        for inner_train_index, inner_val_index in inner_cv.split(X_train):
            X_inner_train, X_inner_val = X_train[inner_train_index], X_train[inner_val_index]
            y_inner_train, y_inner_val = y_train[inner_train_index], y_train[inner_val_index]

            
            ann_model = MLPRegressor(hidden_layer_sizes=(h,), max_iter=10000)
            ann_model.fit(X_inner_train, y_inner_train)
            y_inner_pred = ann_model.predict(X_inner_val)
            ann_errors.append(mean_squared_error(y_inner_val, y_inner_pred))

        # Updating best h if current model is better
        avg_ann_error = np.mean(ann_errors)
        if avg_ann_error < best_ann_error:
            best_ann_error = avg_ann_error
            best_h = h

    # Training final ANN model with best h and calculating error
    final_ann_model = MLPRegressor(hidden_layer_sizes=(best_h,), max_iter=10000).fit(X_train, y_train)
    ann_error = mean_squared_error(y_test, final_ann_model.predict(X_test))

    results_df = results_df._append({
        'Fold': fold,
        'Baseline Error': baseline_error,
        'Optimal λ': best_lambda,
        'Ridge Error': ridge_error,
        'Optimal h': best_h,
        'ANN Error': ann_error
    }, ignore_index=True)

print(results_df)



# Extract error columns for each model
errors_ann = results_df['ANN Error']
errors_ridge = results_df['Ridge Error']
errors_baseline = results_df['Baseline Error']

# Paired t-tests between models
t_stat_ann_vs_ridge, p_val_ann_vs_ridge = stats.ttest_rel(errors_ann, errors_ridge)
t_stat_ann_vs_baseline, p_val_ann_vs_baseline = stats.ttest_rel(errors_ann, errors_baseline)
t_stat_ridge_vs_baseline, p_val_ridge_vs_baseline = stats.ttest_rel(errors_ridge, errors_baseline)

# Calculate the confidence intervals
confidence_level = 0.95
ci_ann_vs_ridge = stats.t.interval(confidence_level, len(errors_ann)-1, loc=np.mean(errors_ann - errors_ridge), scale=stats.sem(errors_ann - errors_ridge))
ci_ann_vs_baseline = stats.t.interval(confidence_level, len(errors_ann)-1, loc=np.mean(errors_ann - errors_baseline), scale=stats.sem(errors_ann - errors_baseline))
ci_ridge_vs_baseline = stats.t.interval(confidence_level, len(errors_ridge)-1, loc=np.mean(errors_ridge - errors_baseline), scale=stats.sem(errors_ridge - errors_baseline))

# Print the results
print(f"ANN vs. Linear Regression: t-statistic = {t_stat_ann_vs_ridge}, p-value = {p_val_ann_vs_ridge}, CI = {ci_ann_vs_ridge}")
print(f"ANN vs. Baseline: t-statistic = {t_stat_ann_vs_baseline}, p-value = {p_val_ann_vs_baseline}, CI = {ci_ann_vs_baseline}")
print(f"Linear Regression vs. Baseline: t-statistic = {t_stat_ridge_vs_baseline}, p-value = {p_val_ridge_vs_baseline}, CI = {ci_ridge_vs_baseline}")



X = df.drop('num', axis=1)
y = df['num']


numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)
X_processed = preprocessor.fit_transform(X)



# Defining the classification models
logistic_model = LogisticRegression(penalty='l2', C=opt_lambda, solver='lbfgs', max_iter=10000)
ann_model = MLPClassifier(hidden_layer_sizes=(best_h,), activation='tanh', max_iter=10000)
baseline_model = DummyClassifier(strategy='most_frequent')


cv_outer = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
logistic_scores = cross_val_score(logistic_model, X_processed, y, cv=cv_outer, scoring='accuracy')
ann_scores = cross_val_score(ann_model, X_processed, y, cv=cv_outer, scoring='accuracy')
baseline_scores = cross_val_score(baseline_model, X_processed, y, cv=cv_outer, scoring='accuracy')


t_stat_log_baseline, p_log_baseline = ttest_rel(logistic_scores, baseline_scores)
t_stat_ann_baseline, p_ann_baseline = ttest_rel(ann_scores, baseline_scores)
t_stat_log_ann, p_log_ann = ttest_rel(logistic_scores, ann_scores)

print("Paired t-test results:")
table_data_ttest = [
    ("Model Comparison", "t-statistic", "p-value"),
    ("Logistic vs Baseline", t_stat_log_baseline, p_log_baseline),
    ("ANN vs Baseline", t_stat_ann_baseline, p_ann_baseline),
    ("Logistic vs ANN", t_stat_log_ann, p_log_ann)
]
print(tabulate(table_data_ttest, headers="firstrow", tablefmt="pretty"))


# Training the models on the dataset
final_logistic_model = logistic_model.fit(X_processed, y)
final_ann_model = ann_model.fit(X_processed, y)
final_baseline_model = baseline_model.fit(X_processed, y)


# Making predictions
predictions = final_logistic_model.predict(X_processed)
predictions_logistic = final_logistic_model.predict(X_processed)
predictions_ann = final_ann_model.predict(X_processed)
predictions_baseline = final_baseline_model.predict(X_processed)

# Evaluateing feature importance
importance = final_logistic_model.coef_


feature_names = preprocessor.get_feature_names_out()
feature_importance = dict(zip(feature_names, importance.flatten()))


print("\nFeature Importance:")
table_data_feature_importance = [(feature, importance) for feature, importance in feature_importance.items()]
print(tabulate(table_data_feature_importance, headers=["Feature", "Importance"], tablefmt="pretty"))


accuracy = accuracy_score(y, predictions)
precision = precision_score(y, predictions, average='weighted')
recall = recall_score(y, predictions, average='weighted')
f1 = f1_score(y, predictions, average='weighted')
conf_matrix = confusion_matrix(y, predictions)

# Printing classification metrics
print("Classification Metrics:")
table_data_metrics = [
    ("Metric", "Value"),
    ("Accuracy", accuracy),
    ("Precision", precision),
    ("Recall", recall),
    ("F1 Score", f1)
]
print(tabulate(table_data_metrics, headers="firstrow", tablefmt="pretty"))

## Classification Part 3

y_true = df['num']


# Creating confusion matrices for both models
conf_matrix_model1 = confusion_matrix(y_true, predictions_logistic)
conf_matrix_model2 = confusion_matrix(y_true, predictions_ann)
conf_matrix_model3 = confusion_matrix(y_true, predictions_baseline)

table_1_2 = mcnemar_table(y_target=y_true, y_model1=predictions_logistic, y_model2=predictions_ann)
table_1_3 = mcnemar_table(y_target=y_true, y_model1=predictions_logistic, y_model2=predictions_baseline)
table_2_3 = mcnemar_table(y_target=y_true, y_model1=predictions_ann, y_model2=predictions_baseline)

# Performing McNemar's test
m1_2 = mcnemar(table_1_2)
m1_3 = mcnemar(table_1_3)
m2_3 = mcnemar(table_2_3)


plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix_model1, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix - Logistic")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix_model2, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix - ANN")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix_model3, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix - Baseline")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()


print("McNemar's Test:\n\n")

print("Logistic vs. ANN:")
print("Statistic:", m1_2[0])
print("P-value:", m1_2[1])

print("Logistic vs. Baseline:")
print("Statistic:", m1_3[0])
print("P-value:", m1_3[1])

print("ANN vs. Baseline:")
print("Statistic:", m2_3[0])
print("P-value:", m2_3[1])


alpha = 0.05
if m1_2[1] < alpha:
    print("There is a significant difference between Logistic and ANN.")
else:
    print("There is no significant difference between the Logistic and ANN.")

if m1_3[1] < alpha:
    print("There is a significant difference between Logistic and Baseline.")
else:
    print("There is no significant difference between Logistic and Baseline.")

if m2_3[1] < alpha:
    print("There is a significant difference between ANN and Baseline.")
else:
    print("There is no significant difference between ANN and Baseline.")


## Classification Part 5

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logistic_model = LogisticRegression(penalty='l2', C=1.0, solver='lbfgs', max_iter=10000)
logistic_model.fit(X_train_scaled, y_train)

predictions = logistic_model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

# Plotting confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

## Classification Part 4

method2_params = {'k': range(1, 51)}  
logistic_params = {'C': np.logspace(-2, 2, 50)}  
baseline_params = {}  


outer_cv = KFold(n_splits=10, shuffle=True, random_state=42)
results = []

for i, (train_index, test_index) in enumerate(outer_cv.split(X)):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]


    # Creating models with the best parameters
    model_method2 = MLPClassifier(hidden_layer_sizes=(best_h,), activation='tanh', max_iter=10000)
    model_logistic = LogisticRegression(penalty='l2', C=opt_lambda, solver='lbfgs', max_iter=10000)
    model_baseline = DummyClassifier(strategy='most_frequent')

    # Fitting models
    model_method2.fit(X_train, y_train)
    model_logistic.fit(X_train, y_train)
    model_baseline.fit(X_train, y_train)

    # Evaluating models
    y_pred_method2 = model_method2.predict(X_test)
    y_pred_logistic = model_logistic.predict(X_test)
    y_pred_baseline = model_baseline.predict(X_test)

    # Calculating error rates
    error_method2 = 1 - accuracy_score(y_test, y_pred_method2)
    error_logistic = 1 - accuracy_score(y_test, y_pred_logistic)
    error_baseline = 1 - accuracy_score(y_test, y_pred_baseline)

    # Storing results
    results.append({
        'Outer Fold': i+1,
        'Method 2': best_h,
        'Error Method 2': error_method2,
        'Logistic Regression': opt_lambda,
        'Error Logistic': error_logistic,
        'Baseline': '-',  # Baseline has no parameters
        'Error Baseline': error_baseline,
    })

results_df = pd.DataFrame(results)
print(results_df)
