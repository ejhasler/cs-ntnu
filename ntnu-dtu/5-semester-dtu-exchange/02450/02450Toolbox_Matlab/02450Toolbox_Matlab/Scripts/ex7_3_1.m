% exercise 7.3.1. Test appropriate for Setup II
ex5_1_5;
% Construct a regression problem where the goal is to predict alcohol
% content based on attributes 1--10.
y = X(:,11); 
X = X(:,1:10);
% split into a training and test set.
rng('default');
K = 10; 
m = 2; % repeated cross validation.
J = 0; % repated cross-validations.
r = [];
for dm=1:m
    CV = cvpartition(N, 'Kfold', K);
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
        
        % calculate average difference in loss for this fold. 
        loss = 1; 
        r(end+1) = mean( abs( yfitA-y_test ).^loss - abs( yfitB-y_test).^loss );        
    end
end
%%
alpha = 0.05; 
rho = 1/K; 
[p_setupII, CI_setupII] = correlated_ttest(r, rho, alpha);
%% perform statistical comparison of the models using setupI. 
if m == 1
    % note our usual setup I ttest only makes sense if m=1. 
    zA = abs(y_true - yhat(:,1) ).^loss;
    zB = abs(y_true - yhat(:,2) ).^loss;
    z = zA - zB;
    [~, p_setupI, CI_setupI] = ttest( z, [], 'alpha', alpha);

    [p_setupII, p_setupI]
    [CI_setupII ; CI_setupI']
end