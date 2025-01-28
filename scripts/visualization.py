import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column, bins=30, title="Histogram", xlabel="Value", ylabel="Frequency", color='blue'):
    """
    Plots a histogram for a given column in the dataframe.
    """
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=bins, alpha=0.7, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_scatter(df, x_column, y_column, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Plots a scatter plot for two given columns in the dataframe.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_column, y=y_column, data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_correlation_heatmap(df, columns, title="Correlation Matrix", cmap='coolwarm'):
    """
    Plots a heatmap of the correlation matrix for the given columns.
    """
    correlation_matrix = df[columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap)
    plt.title(title)
    plt.show()

def plot_pca(df, pca_components, title="PCA: Reduced Dimensions"):
    """
    Plots the results of PCA, where pca_components is a dataframe with the PCA results.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_components)
    plt.title(title)
    plt.show()
