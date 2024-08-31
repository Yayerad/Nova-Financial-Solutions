from textblob import TextBlob

def sentiment_analysis(df):
    """
    Perform sentiment analysis on the headlines and categorize the sentiment.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - df (pd.DataFrame): DataFrame with additional columns for sentiment polarity and sentiment category.
    """
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Categorize sentiment
    def categorize_sentiment(score):
        if score > 0:
            return 'positive'
        elif score == 0:
            return 'neutral'
        else:
            return 'negative'

    df['sentiment_category'] = df['sentiment'].apply(categorize_sentiment)
    return df
