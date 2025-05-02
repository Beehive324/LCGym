import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    tweets = tweets.query('content.str.len() > 15')
    tweets = tweets.drop(columns=['content'])

    return tweets

    





    