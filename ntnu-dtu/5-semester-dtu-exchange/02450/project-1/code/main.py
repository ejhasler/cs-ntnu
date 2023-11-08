import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from ucimlrepo import fetch_ucirepo 

# @authors
# Jørgen Finsveen
# Even J. P. Haslerud


# Reads dataset and prints first 5 observations
heart_disease = fetch_ucirepo(id=45) 
data = heart_disease.data.features   
data.head()




# Plots box-plots of each attribute in order to detect outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, orient="h")
plt.title("Box Plots of Attributes (Outlier Analysis)")
#plt.show()


# Plots histograms of each attribute for visualizing attribute distribution
data.hist(bins=50, figsize=(30, 15))
plt.suptitle("Attribute Distributions")
#plt.show()


# Plotting correlation matrix/heatmap 
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
#plt.show()


# Standardizing and transforming features as a preperation for PCA
data = data.dropna(axis=1) # Drops columns with NaN values in order to perform PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data) 


# Plotting diagram of Principal Component Analysis
pca = PCA()
pca.fit(scaled_data)

explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Variance Explained by PCA Components")
plt.show()