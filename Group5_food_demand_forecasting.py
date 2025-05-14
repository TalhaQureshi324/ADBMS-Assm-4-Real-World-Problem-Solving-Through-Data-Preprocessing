import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import os

def merge_csv_files():
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]
    df_list = []
    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def describe_attributes(df):
    print("\n=== Data Types ===\n", df.dtypes)
    print("\n=== First Few Rows ===\n", df.head())
    print("\n=== Basic Info ===\n")
    df.info()
    print("\n=== Statistical Summary ===\n", df.describe(include='all'))

def visualize_distributions(df, before=True):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        plt.figure(figsize=(10, 5))
        if df[col].nunique() <= 2:
            sns.stripplot(data=df, x=np.zeros(df.shape[0]), y=col, jitter=True, alpha=0.3)
            plt.title(f"{'Before' if before else 'After'} Outlier Removal - Binary Feature: {col}")
            plt.ylabel(col)
            plt.xlabel("Binary Feature Distribution")
        else:
            sns.boxplot(data=df[col])
            plt.title(f"{'Before' if before else 'After'} Outlier Removal - Boxplot: {col}")
        plt.tight_layout()
        plt.savefig(f"{col}_{'before' if before else 'after'}_boxplot.png")
        plt.close()


def remove_outliers(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

def handle_missing(df):
    print("\n=== Missing Values Before ===\n", df.isnull().sum())
    df = df.dropna(how='all')
    df = df.drop_duplicates()
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())
    print("\n=== Missing Values After ===\n", df.isnull().sum())
    return df
def create_visualizations(df):
    df.hist(bins=30, figsize=(15, 10))
    plt.tight_layout()
    plt.savefig("histograms.png")
    plt.close()

    if 'meal_id' in df.columns:
        plt.figure(figsize=(12, 6))
        df['meal_id'].value_counts().nlargest(20).plot(kind='bar')
        plt.title("Top 20 Most Ordered Meals")
        plt.xlabel("Meal ID")
        plt.ylabel("Frequency")
        plt.savefig("top20_products.png")
        plt.close()

    if 'category' in df.columns and 'num_orders' in df.columns:
        le = LabelEncoder()
        df['category_encoded'] = le.fit_transform(df['category'].astype(str))
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='category_encoded', y='num_orders', data=df)
        plt.title("Category vs Number of Orders")
        plt.xlabel("Encoded Category")
        plt.ylabel("Number of Orders")
        plt.savefig("scatter_Product_vs_Demand.png")
        plt.close()


def save_cleaned_dataset(df):
    df.to_csv("CleanedDataset.csv", index=False)
    print("\n✅ Cleaned dataset saved as 'CleanedDataset.csv'.")

def main():
    print("📦 Merging all CSVs...")
    df = merge_csv_files()

    print("🔍 Describing attributes...")
    describe_attributes(df)

    print("📊 Visualizing boxplots BEFORE outlier removal...")
    visualize_distributions(df, before=True)

    print("🧹 Handling missing values...")
    df = handle_missing(df)

    print("❌ Removing outliers...")
    df = remove_outliers(df)

    print("📊 Visualizing boxplots AFTER outlier removal...")
    visualize_distributions(df, before=False)

    print("📈 Creating additional visualizations...")
    create_visualizations(df)

    print("💾 Saving cleaned dataset...")
    save_cleaned_dataset(df)

    print("\n Done! All preprocessing completed.")

if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print("🚨 Missing module detected. Please install all required libraries using:")
        print("pip install pandas matplotlib seaborn scikit-learn")
        print("Error details:", e)

