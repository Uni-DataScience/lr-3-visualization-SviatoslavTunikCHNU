import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # 1. Descriptive Statistics
    print("Descriptive Statistics:")
    # 1. Descriptive Statistics
    print("Descriptive Statistics:")
    print(df.describe())

    # Calculate additional statistics: median and variance
    median_values = df.median()
    variance_values = df.var()
    mode_values = df.mode().iloc[0]

    print("\nMedian for each column:")
    print(median_values)

    print("\nVariance for each column:")
    print(variance_values)

    print("\nMode for each column:")
    print(mode_values)

    # 2. Outlier Detection - Boxplots
    print("\nGenerating Boxplots...")
    for column in df.columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(y=df[column], color='skyblue')
        plt.title(f'Boxplot of {column}')
        plt.tight_layout()
        plt.savefig("mygraph4_1"+ column +".png")

    # 3. Correlation Analysis - Heatmap
    print("\nCorrelation Matrix:")
    corr_matrix = df.corr()
    print(corr_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig("mygraph4_2.png")


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)

