from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def vader_sentiment_analysis(df):
    """
    Perform sentiment analysis on the headlines using VADER and categorize the sentiment.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - df (pd.DataFrame): DataFrame with additional columns for sentiment polarity and sentiment category.
    """
    # Calculate sentiment polarity using VADER
    df['sentiment'] = df['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Function to categorize sentiment based on VADER's compound score
    def categorize_sentiment(score):
        if score > 0.05:
            return 'positive'
        elif score < -0.05:
            return 'negative'
        else:
            return 'neutral'

    # Apply categorization function
    df['sentiment_category'] = df['sentiment'].apply(categorize_sentiment)
    return df
