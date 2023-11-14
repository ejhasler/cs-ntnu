% exercise 7.3.3. Comparing two classifiers
%% Re-compute results used in classification problem.
ex7_1_1
alpha = 0.05;
[thetahat, CI, p] = mcnemar(y_true, yhat(:,1), yhat(:,2), alpha);  
