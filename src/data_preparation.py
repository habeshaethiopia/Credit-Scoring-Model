import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """
    Load the dataset into a Pandas DataFrame.
    """
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        data = pd.read_excel(file_path, engine='openpyxl')  # Use the appropriate engine for .xlsx files
    elif file_path.endswith('.csv'):
        data = pd.read_csv(file_path, encoding='utf-8')
    return data

def clean_data(df, numeric_columns=None):
    """
    Clean the dataset by handling missing values and ensuring correct data types.
    You can pass a list of numeric columns to convert them to numeric types.
    """
    # Drop any rows with missing data
    df = df.dropna()
    
    # If numeric_columns are provided, convert them to numeric types
    if numeric_columns:
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    return df

def aggregate_user_data(df, download_column, upload_column):
    """
    Aggregate user data to compute total data usage and other relevant metrics.
    """
    # Calculate total data usage per user
    df['Total Data (Bytes)'] = df[download_column] + df[upload_column]
    return df

def segment_by_decile(df, column):
    """
    Segments users into deciles based on the provided column.
    """
    df['decile'] = pd.qcut(df[column], 10, labels=False)
    return df

def check_for_outliers(df, numeric_columns):
    """
    Check for outliers in the dataset using boxplots.
    """
    plt.figure(figsize=(10, 6))
    df[numeric_columns].boxplot()
    plt.title("Boxplot of Data Usage by Category")
    plt.show()

def visualize_correlation(df, numeric_columns):
    """
    Visualize the correlation between different data usage columns.
    """
    correlation_matrix = df[numeric_columns].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap of Data Usage Columns")
    plt.show()

def plot_total_data_usage(df, download_column, upload_column):
    """
    Plot total data usage for each entry (Total DL and UL bytes).
    """
    plt.figure(figsize=(10, 6))
    df[download_column].plot(kind='bar', color='blue', alpha=0.6, label='Download')
    df[upload_column].plot(kind='bar', color='red', alpha=0.6, label='Upload')
    plt.title("Total Data Usage (Download vs Upload)")
    plt.xlabel("Index")
    plt.ylabel("Data Usage (Bytes)")
    plt.legend()
    plt.show()

def plot_top_categories(df, categories):
    """
    Visualize top data usage categories (e.g., Gaming, Netflix, Youtube).
    Pass a list of category columns to aggregate and plot.
    """
    total_usage = df[categories].sum()
    
    plt.figure(figsize=(8, 6))
    total_usage.plot(kind='bar', color=['blue', 'green', 'red', 'orange'])
    plt.title("Total Download Data Usage by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Data (Bytes)")
    plt.show()

def plot_interactive(df, x_column, y_column, color_column):
    """
    Create an interactive dashboard using Plotly for total data usage.
    You can pass any columns for x, y, and color.
    """
    fig = px.scatter(df, x=x_column, y=y_column, 
                     color=color_column, 
                     title=f"Interactive Scatter Plot of {x_column} vs {y_column}",
                     labels={x_column: f'{x_column} (Bytes)', y_column: f'{y_column} (Bytes)'})
    fig.show()

def get_top_consumers(df, data_column, top_n=10):
    """
    Get the top 'n' consumers of data (by total usage).
    """
    top_consumers = df.nlargest(top_n, data_column)
    return top_consumers[['Last Location Name', data_column]]

def get_usage_by_service(df, services):
    """
    Calculate total data usage by service (e.g., YouTube, Netflix, Gaming).
    Pass a list of service columns to aggregate the total usage.
    """
    usage_by_service = df[services].sum()
    return usage_by_service

def calculate_growth(df, download_column, upload_column):
    """
    Estimate potential growth by comparing usage between download and upload categories.
    """
    df['Total Download Growth'] = (df[download_column] - df[upload_column]) / df[upload_column]
    return df[['Last Location Name', 'Total Download Growth']]

def describe_data(df):
    """
    Get basic statistics about the dataset.
    """
    return df.describe()

def plot_histogram(df, column, bins=30, title="Histogram"):
    """
    Plot a histogram for a specified column of the dataframe.
    """
    plt.figure(figsize=(10, 6))
    df[column].plot(kind='hist', bins=bins, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_scatter(df, x_column, y_column, title="Scatter Plot"):
    """
    Plot a scatter plot for two specified columns of the dataframe.
    """
    plt.figure(figsize=(10, 6))
    df.plot(kind='scatter', x=x_column, y=y_column, color='blue')
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_correlation_heatmap(df, columns, title="Correlation Heatmap"):
    """
    Plot a correlation heatmap for a subset of columns in the dataframe.
    """
    correlation_matrix = df[columns].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(title)
    plt.show()

def plot_pca(df, title="PCA Plot"):
    """
    Plot PCA results after dimensionality reduction.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['PC1'], df['PC2'], color='blue')
    plt.title(title)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()
