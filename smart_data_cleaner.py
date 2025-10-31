import pandas as pd
import numpy as np

class SmartDataCleaner:
    """
    Smart Analyst: Data Cleaner Module
    Cleans, fixes, and summarizes data issues automatically.
    """

    def __init__(self, strategy='mean', outlier_threshold=3):
        self.strategy = strategy
        self.outlier_threshold = outlier_threshold
        self.report = {}

    def clean(self, df: pd.DataFrame):
        df_cleaned = df.copy()

        # Normalize string data
        df_cleaned = df_cleaned.applymap(
            lambda x: x.strip().lower() if isinstance(x, str) else x
        )

        # Handle missing values
        num_cols = df_cleaned.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if self.strategy == 'mean':
                df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            elif self.strategy == 'median':
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
            elif self.strategy == 'mode':
                df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)

        # Remove duplicates
        before = df_cleaned.shape[0]
        df_cleaned.drop_duplicates(inplace=True)
        after = df_cleaned.shape[0]
        self.report['duplicates_removed'] = before - after

        # Handle outliers
        for col in num_cols:
            mean = df_cleaned[col].mean()
            std = df_cleaned[col].std()
            upper = mean + self.outlier_threshold * std
            lower = mean - self.outlier_threshold * std
            outliers = ((df_cleaned[col] < lower) | (df_cleaned[col] > upper))
            df_cleaned.loc[outliers, col] = np.nan
            df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)

        # Update report
        self.report['missing_values_fixed'] = int(df_cleaned.isna().sum().sum())
        self.report['final_shape'] = df_cleaned.shape

        return df_cleaned, self.report

