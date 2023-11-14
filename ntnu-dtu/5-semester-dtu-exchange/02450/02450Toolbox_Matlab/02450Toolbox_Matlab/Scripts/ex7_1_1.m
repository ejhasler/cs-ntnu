% exercise 7.3.1. Evaluation of a classifier
% Load data
ex4_2_1

% Leave-one-out crossvalidation
CV = cvpartition(N, 'Leaveout');
K = CV.NumTestSets;

% K-nearest neighbors parameters
Distance = 'euclidean'; % Distance measure
L = [1,20,80]; % Maximum number of neighbors

% Variable for classification error
Error = nan(K,length(L));

yhat = [];
y_true = [];
for k = 1:K % For each crossvalidation fold
    fprintf('Crossvalidation fold %d/%d\n', k, CV.NumTestSets);

    % Extract training and test set
    X_train = X(CV.training(k), :);
    y_train = y(CV.training(k));
    X_test = X(CV.test(k), :);
    y_test = y(CV.test(k));

    y_true(k,1) = y_test(1); 
    
    for l = 1:length(L) % For each number of neighbors        
        % Use knnclassify to find the l nearest neighbors
        knn=fitcknn(X_train, y_train, 'NumNeighbors', L(l), 'Distance', Distance);
        y_test_est=predict(knn, X_test);
        
        % Compute number of classification errors
        Error(k,l) = sum(y_test~=y_test_est); % Count the number of errors
        yhat(k,l) = y_test_est(1);  
    end
end
%% Compute accuracy of the three models here using y_true and yhat here
% 