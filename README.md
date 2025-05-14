
# 📊 Food Demand Forecasting - Data Preprocessing Project

This project aims to preprocess real-world food demand data to prepare it for advanced analytics and forecasting. The pipeline is implemented in Python and automates dataset merging, data cleaning, outlier handling, and visualization generation.

---

## 📁 Dataset Overview

- **Source**: Kaggle dataset on Food Demand Forecasting https://www.kaggle.com/datasets/kannanaikkal/food-demand-forecasting
- **Files**: 5 CSV files containing information on centers, meals, demand, pricing, etc.
- **Final Dataset Shape**: ~310,000 rows × 15 columns

---

## ⚙️ Features and Workflow

1. **Merge All CSVs**
   - Automatically detects and merges all `.csv` files in the directory.

2. **Explore Data**
   - Prints column types, missing values, and statistical summaries.

3. **Handle Missing Values**
   - Uses `mode()` for categorical and `median()` for numeric values.

4. **Remove Outliers**
   - Uses IQR (Interquartile Range) method for numeric columns.

5. **Visualizations**
   - Boxplots before and after cleaning
   - Histograms
   - Top 20 most frequent meals (bar chart)
   - Category vs Demand (scatter plot)

6. **Save Clean Dataset**
   - Exports the cleaned DataFrame as `CleanedDataset.csv`

---

## ⚠️ Important Note

🧹 **Please DELETE `CleanedDataset.csv` before running the script again!**  
If you do not delete it, it may interfere with the merging process or result in duplicate entries.

---

## 📸 Output Files

- `*_before_boxplot.png` and `*_after_boxplot.png` of every column
- `histograms.png`
- `top20_products.png`
- `scatter_Product_vs_Demand.png`
- `CleanedDataset.csv`

---

## 💻 Run Instructions

Make sure you have Python installed along with required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Then simply run:

```bash
python Group5_food_demand_forecasting.py
```

## 🙋 Author

This project was completed as part of a university data preprocessing assignment and includes all mandatory components like code, documentation, and visual outputs.
Muhammad Talha (BSCS23122)

---
