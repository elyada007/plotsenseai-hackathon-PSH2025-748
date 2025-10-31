import streamlit as st
import pandas as pd
from smart_data_cleaner import SmartDataCleaner

st.set_page_config(page_title="Smart Data Cleaner", page_icon="🧹", layout="wide")

st.title(" Smart Data Cleaner (PlotSenseAI Module)")
st.write("Automatically clean, fix, and summarize your dataset.")

# File uploader
uploaded_file = st.file_uploader(" Upload a CSV file to clean", type=["csv"])

# Options
strategy = st.selectbox(
    "Missing Value Strategy:",
    ["mean", "median", "mode"],
    index=0
)
outlier_threshold = st.slider(
    "Outlier Detection Threshold (Standard Deviations):", 1, 5, 3
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader(" Original Data Preview")
    st.dataframe(df.head())

    if st.button(" Clean Data"):
        cleaner = SmartDataCleaner(strategy=strategy, outlier_threshold=outlier_threshold)
        cleaned_df, report = cleaner.clean(df)

        st.success("✅ Data Cleaning Completed!")

        st.subheader(" Cleaned Data Preview")
        st.dataframe(cleaned_df.head())

        st.subheader(" Cleaning Report")
        st.json(report)

        # Download button
        csv = cleaned_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇ Download Cleaned CSV",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv",
        )
else:
    st.info(" Upload a CSV file to get started.")
