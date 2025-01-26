import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """
    Load the dataset into a Pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """
    Clean the dataset by handling missing values and ensuring correct data types.
    """
    # Drop rows with missing values
    df = df.dropna()

    # Convert relevant columns to numeric, forcing errors to NaN for non-numeric values
    numeric_columns = [
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 
        'Netflix UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 
        'Other DL (Bytes)', 'Other UL (Bytes)', 'Total DL (Bytes)', 'Total UL (Bytes)'
    ]
    # Automatically detect numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    return df

def get_basic_statistics(df):
    """
    Get basic descriptive statistics of the dataset.
    """
    return df.describe()

def visualize_data_distribution(df):
    """
    Visualize the distribution of key columns using histograms.
    """
    numeric_columns = [
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 
        'Netflix UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 
        'Other DL (Bytes)', 'Other UL (Bytes)', 'Total DL (Bytes)', 'Total UL (Bytes)'
    ]
    
    # Plot histograms for each of the numeric columns
    df[numeric_columns].hist(bins=20, figsize=(15, 10), edgecolor='black')
    plt.suptitle("Data Distribution of Key Columns")
    plt.show()

def plot_boxplots(df):
    """
    Visualize boxplots for identifying outliers in the data.
    """
    numeric_columns = [
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 
        'Netflix UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 
        'Other DL (Bytes)', 'Other UL (Bytes)', 'Total DL (Bytes)', 'Total UL (Bytes)'
    ]
    
    # Plot boxplots to visualize outliers for each numeric column
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=df[numeric_columns], orient='h', palette="Set2")
    plt.title("Boxplot for Data Usage (Identifying Outliers)")
    plt.show()

def visualize_correlations(df):
    """
    Visualize the correlations between various data usage categories using a heatmap.
    """
    correlation_matrix = df.corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap of Data Usage Columns")
    plt.show()

def plot_top_consumers(df, top_n=10):
    """
    Identify the top consumers of data and visualize them.
    """
    df['Total Data Usage'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    top_consumers = df.nlargest(top_n, 'Total Data Usage')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Total Data Usage', y='Last Location Name', data=top_consumers, palette='viridis')
    plt.title(f"Top {top_n} Data Consumers")
    plt.xlabel("Total Data Usage (Bytes)")
    plt.ylabel("Location Name")
    plt.show()

def plot_category_usage(df):
    """
    Visualize total data usage by category (YouTube, Netflix, Gaming, etc.)
    """
    categories = [
        'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)', 'Other DL (Bytes)'
    ]
    total_usage_by_category = df[categories].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    total_usage_by_category.plot(kind='bar', color=['blue', 'green', 'red', 'orange'])
    plt.title("Total Data Download Usage by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Data Usage (Bytes)")
    plt.show()

def interactive_scatter_plot(df):
    """
    Create an interactive scatter plot to explore the relationship between download and upload data.
    """
    fig = px.scatter(df, x='Total DL (Bytes)', y='Total UL (Bytes)', 
                     color='Last Location Name', 
                     title="Interactive Scatter Plot: Total Download vs Upload Data",
                     labels={'Total DL (Bytes)': 'Download (Bytes)', 'Total UL (Bytes)': 'Upload (Bytes)'})
    fig.show()

def calculate_growth_potential(df):
    """
    Estimate potential growth by comparing the download and upload data usage.
    """
    df['Download Upload Ratio'] = df['Total DL (Bytes)'] / df['Total UL (Bytes)']
    return df[['Last Location Name', 'Download Upload Ratio']].sort_values(by='Download Upload Ratio', ascending=False)

def analyze_user_behavior(df):
    """
    Analyze user behavior by aggregating total data usage and providing insights.
    """
    df['Total Data Usage'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    
    # Analyze average data usage per user
    avg_data_usage = df['Total Data Usage'].mean()
    stdev_data_usage = df['Total Data Usage'].std()
    
    print(f"Average Data Usage: {avg_data_usage:.2f} Bytes")
    print(f"Standard Deviation of Data Usage: {stdev_data_usage:.2f} Bytes")
    
    return avg_data_usage, stdev_data_usage
