% exercise 8.3.3
clear all;
% Load data
cdir = fileparts(mfilename('fullpath'));
load(fullfile(cdir,'../Data/synth2'))

%% Fit regularized multinomial regression model
% Standardize based on training set
mu = mean(X_train,1);
sigma = std(X_train,1);
X_train = bsxfun(@times, X_train - mu, 1./ sigma);
X_test = bsxfun(@times, X_test - mu, 1./ sigma);

% Define the softmax loss for multinomial logistic regression
funObj = @(W)SoftmaxLoss2(W, ...
            [ones(length(X_train),1) X_train], ...
            y_train+1,C);

% Setup the reguliarzation parameter
regularization_strength = 1e3; 
% Try a  high regularization strength, e.g. 1e3, especially for synth2,
% synth3 and synth 4, and investigate the estimated distributions

lambda = regularization_strength*ones(M+1,C-1);i
lambda(1,:) = 0; % Don't penalize biases
options = [];

% Train the model using fminunc
fprintf('Training multinomial logistic regression model...\n');
wSoftmax = fminunc(@penalizedL2,zeros((M+1)*(C-1),1), ...
                    options,funObj,lambda(:));
%wSoftmax = minFunc(@penalizedL2, zeros((M+1)*(C-1),1), ...
%                       options, funObj, lambda(:));
% Notice that we fit to obtain weights for C-1 classes. We now reshape the
% weights such that each row represents an attribute (including the bias)
% and each column represent a class, representing the last class by zero
% weights
wSoftmax = reshape(wSoftmax,[M+1 C-1]);
wSoftmax = [wSoftmax zeros(M+1,1)];

% Predict the class of the test set using the fitted model
[~, y_test_est] = max([ones(length(X_test),1) X_test]*wSoftmax,[],2);
y_test_est = y_test_est-1;

% Compute error rate
ErrorRate = sum( y_test ~= y_test_est ) / N_test;
fprintf('Error rate: %.0f%%\n', ErrorRate * 100);
 
%% Plot results
% Display decision boundaries
mfig('Decision Boundaries'); clf;
dbplot(X_test, y_test, @(X) max_idx([ones(length(X),1) X]*wSoftmax)-1);
xlabel(attributeNames(1));
ylabel(attributeNames(2));

%% Effect of high regularization strength
% Make a plot of the distribution of the training set labels and the
% estimated labels. Try using a very high regularization strength, e.g.
% 1e10, how does that affect the estimates (which label dominates in the 
% estimations)? Try relating this effect to the regularized linear
% regression with very high regularization strength. 

edges = unique(y)-.5;
edges(C+1) = edges(C)+1
counts = [  histcounts(y_train, edges,'normalization','probability'); ...
            histcounts(y_test, edges,'normalization','probability'); ...
            histcounts(y_test_est, edges, 'normalization','probability') ]';

mfig('True label and estimated label distributions')
    bar(counts)
    ylim([0 1])
    ylabel('Probability')
    xlabel('Label')
    legend('Training set', 'Test set', 'Test estimates', 'Location','best')
    grid minor
   

%% (OPTIONAL) High performance fitting
% If you need to train e.g. large data sets or with many input features, it
% would likely be beneficial to use the minFunc software available in the
% toolbox. 
% To use the minFunc-function you would then replace the call to fminunc
% above with the following lines:
%
%   wSoftmax = minFunc(@penalizedL2, zeros((M+1)*(C-1),1), ...
%                       options, funObj, lambda(:));
%
% You might need to compile the needed mex-files for your machine. You can
% do this by running:
%
%   cd(fullfile(cdir,'../Tools/minFunc_2012')); mexAll; cd(cdir);
%
% You might, in turn, need to have installed the proper compiler, in which
% case you should simply follow the instructions in the message that comes
% when running the mexAll.m. 