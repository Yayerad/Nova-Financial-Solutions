import pandas as pd

def headline_length_stats(df):
    """
    Calculate basic statistics for headline lengths.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - stats (pd.Series): Series with the headline length statistics.
    """
    df['headline_length'] = df['headline'].apply(len)
    stats = df['headline_length'].describe()
    return stats

def articles_per_publisher(df):
    """
    Count the number of articles per publisher.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - publisher_counts (pd.Series): Series with the counts of articles per publisher.
    """
    publisher_counts = df['publisher'].value_counts()
    return publisher_counts
