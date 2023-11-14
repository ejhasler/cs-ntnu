% exercise 7.3.2. Evaluation of a classifier
%% Re-compute results
ex7_1_1
alpha = 0.05; 
[thetahatA, CIA] = jeffrey_interval(y_true, yhat(:,1), alpha);
