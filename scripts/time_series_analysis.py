# scripts/time_series_analysis.py

import pandas as pd

def publication_trends(df):
    """
    Analyze the publication trends over time.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - trends (pd.Series): Series with counts of articles published per day.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Parse date and handle potential errors
    trends = df.groupby(df['date'].dt.date).size()
    return trends
