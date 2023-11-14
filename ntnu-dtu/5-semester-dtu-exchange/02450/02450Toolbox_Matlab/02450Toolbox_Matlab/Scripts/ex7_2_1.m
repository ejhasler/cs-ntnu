% exercise 7.2.1

ex5_1_5;
% Construct a regression problem where the goal is to predict alcohol
% content based on attributes 1--10.
y = X(:,11); 
X = X(:,1:10);
% split into a training and test set.
rng(1)
K = 1;
CV = cvpartition(N, 'HoldOut', 0.2);
%K = 10; 
%CV = cvpartition(N, 'Kfold', K);

% For each crossvalidation fold
y_true = [];
yhat = [];
for k = 1:K
    fprintf('Crossvalidation fold %d/%d\n', k, K);    
    % Extract the training and test set
    X_train = X(CV.training(k), :);
    y_train = y(CV.training(k));
    X_test = X(CV.test(k), :);
    y_test = y(CV.test(k));
        
    %% Train a linear regression model (Model A). 
    % see script from exercise 5.2.3 for details
    w_est = glmfit(X_train, y_train, 'normal');
    yfitA = glmval(w_est, X_test, 'identity');
    %%
    %% Train and test a regression tree (model B).
    tree = fitrtree(X_train, y_train);
    yfitB = tree.predict(X_test);
    %% Gather results
    y_true = [y_true ; y_test];
    yhat = [yhat ; [yfitA, yfitB]];
end
%% perform statistical comparison of the models
% compute z with squared error.
zA = abs(y_true - yhat(:,1) ).^2;
%% compute confidence interval of model A
alpha = 0.05;
[~, ~, CIA] = ttest( zA, [], 'alpha', alpha);
%% compute confidence interval of z=zA-zB and p-value of Null hypothesis
zB = abs(y_true - yhat(:,2) ).^2;
z = zA - zB;
[~, p, CI] = ttest( z, [], 'alpha', alpha);
