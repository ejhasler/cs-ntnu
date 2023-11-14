% exercise 11.1.5

% Load data
cdir = fileparts(mfilename('fullpath')); 
load(fullfile(cdir,'../Data/synth1'));

%% Gaussian mixture model

% Range of K's to try
KRange = 1:10;
T = length(KRange);

% Allocate variables
BIC = nan(T,1);
AIC = nan(T,1);
CVE = zeros(T,1);

% Create crossvalidation partition for evaluation
CV = cvpartition(N, 'Kfold', 10);

% For each model order
for t = 1:T    
    % Get the current K
    K = KRange(t);
    
    % Display information
    fprintf('Fitting model for K=%d\n', K);
    
    % Fit model
    reg = 0.01;
    G = fitgmdist(X,K,'RegularizationValue',0.01); % Add a little regularization to avoid errors. 
    
    % Get BIC and AIC
    BIC(t) = G.BIC;
    AIC(t) = G.AIC;
    
    % For each crossvalidation fold
    for k = 1:CV.NumTestSets
        % Extract the training and test set
        X_train = X(CV.training(k), :);
        X_test = X(CV.test(k), :);
        
        % Fit model to training set
        G = fitgmdist(X_train,K,'RegularizationValue',0.01);
        
        % Evaluation crossvalidation error
        [~, NLOGL] = posterior(G, X_test);
        CVE(t) = CVE(t)+NLOGL;
    end
end


%% Plot results

mfig('GMM: Number of clusters'); clf; hold all
plot(KRange, BIC);
plot(KRange, AIC);
plot(KRange, 2*CVE);
legend('BIC', 'AIC', 'Crossvalidation');
xlabel('K');
