% exercise 8.1.2

% Load data
cdir = fileparts(mfilename('fullpath')); 
load(fullfile(cdir,'../Data/wine2'))

%% Crossvalidation
% Create crossvalidation partition for evaluation
% using stratification and 95 pct. split between training and test 
CV = cvpartition(classNames(y+1), 'Holdout', .95);

% Extract the training and test set
X_train = X(CV.training, :);
y_train = y(CV.training);
X_test = X(CV.test, :);
y_test = y(CV.test);

% Standardize the data
mu = mean(X_train,1);
sigma = std(X_train,1);
X_train_std = bsxfun(@times, X_train - mu, 1./ sigma);
X_test_std = bsxfun(@times, X_test - mu, 1./ sigma);

%% Fit model
% Fit regularized logistic regression model to training data to predict 
% the type of wine
lambda = logspace(-8,0,50);
test_error_rate = nan(length(lambda),1);
train_error_rate = nan(length(lambda),1);
coefficient_norm = nan(length(lambda),1);
for k = 1:length(lambda)
    mdl = fitclinear(X_train_std, y_train, ...
                 'Lambda', lambda(k), ...
                 'Learner', 'logistic', ...
                 'Regularization', 'ridge');
    [y_train_est, p] = predict(mdl, X_train_std);
    train_error_rate(k) = sum( y_train ~= y_train_est ) / length(y_train);
    
    [y_test_est, p] = predict(mdl, X_test_std);
    test_error_rate(k) = sum( y_test ~= y_test_est ) / length(y_test);
    
    coefficient_norm(k) = norm(mdl.Beta,2);
end
[min_error,lambda_idx] = min(test_error_rate);

%%
mfig('Logistic regression: optimal regularization strength'); clf;
subplot(3,1,1)
    semilogx(lambda, test_error_rate*100)
    hold on
    semilogx(lambda, train_error_rate*100)
    xlabel('Regularization strength (\lambda)')
    ylabel('Error rate (%)')
    ylim([0 10])
    xlim([min(lambda) max(lambda)])
    title('Error rate')
    legend(['Test error, n=', num2str(length(y_test))], ...
           ['Training Error, n=', num2str(length(y_train))])
    grid minor
    
subplot(3,1,2)
    semilogx(lambda, test_error_rate*100)
    hold on
    semilogx(lambda, train_error_rate*100)
    title('Error rate (zoom)')
    xlabel('Regularization strength (\lambda)')
    ylabel('Error rate (%)')
    xlim([1e-6 1e0])
    ylim([0 2.5])
     text(1.5e-6, 2.25, ['Minimum test error: ', num2str(min_error*100,3), ' % at \lambda=1e', ...
        num2str(log10(lambda(lambda_idx)),2)], ...
        'FontSize',16)
    grid minor
    
subplot(3,1,3)
    semilogx(lambda, coefficient_norm,'k')
    xlabel('Regularization strength (\lambda)')
    ylabel('L2 norm of parameter vector')
    title('Parameter vector norm')
    xlim([min(lambda) max(lambda)])
    grid minor




