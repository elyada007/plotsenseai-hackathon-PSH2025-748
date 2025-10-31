# 🧠 PlotSenseAI Data Modules  
**Heatmap Visualization** & **SmartDataCleaner**

---

## 📊 Overview
These modules form part of the **PlotSenseAI** analytical suite — tools designed to make data cleaning and visualization intelligent, automated, and user-friendly.

- **SmartDataCleaner** automatically detects and fixes data quality issues such as missing values, duplicates, inconsistent text entries, and statistical outliers.  
- **Heatmap Generator** provides an intuitive visual summary of data correlations or activity intensity across dimensions — perfect for exploratory data analysis (EDA).

Together, they enhance the PlotSenseAI workflow by combining **data hygiene automation** with **AI-powered visual insights**.

---

## SmartDataCleaner

### 🧩 Description
The **SmartDataCleaner** is an intelligent data preprocessing module that:
- Cleans raw datasets automatically  
- Handles missing values using configurable strategies (`mean`, `median`, or `mode`)  
- Normalizes string data (removes hidden duplicates caused by spacing/case)  
- Detects and replaces outliers based on standard deviation thresholds  
- Generates a simple cleaning report for transparency and tracking  

### 💡 Features
| Function | Description |
|-----------|--------------|
| **Missing Value Handling** | Replaces NaN values using mean, median, or mode |
| **Duplicate Removal** | Detects and removes identical rows |
| **Outlier Correction** | Identifies and replaces outliers with representative values |
| **Normalization** | Cleans string data (trims, converts to lowercase) |
| **Report Generation** | Summarizes cleaning operations performed |
