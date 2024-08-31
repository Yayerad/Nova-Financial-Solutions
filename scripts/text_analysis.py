# scripts/text_analysis.py

from textblob import TextBlob

def sentiment_analysis(df):
    """
    Perform sentiment analysis on the headlines.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - df (pd.DataFrame): DataFrame with an additional column for sentiment polarity.
    """
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df
