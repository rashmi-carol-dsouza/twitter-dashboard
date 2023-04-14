import pandas as pd
import tweepy
def ingestion(words):
    # Creating an empty dataframe to add data extracted from twitter
    db = pd.DataFrame(columns=['id',"time",'text'])
    # Declaring keys for api access
    consumer_key = "enter_consumer_key"
    consumer_secret = "enter_consumer_secret"
    access_key = "enter_access_key"
    access_secret = "enter_access_secret"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    # We are using .Cursor() to search
    # through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets,
                           words, lang="en",
                           since_id="2022-12-01",
                           tweet_mode='extended').items(5000)
        # .Cursor() returns an iterable object. Each item in
        # the iterator has various attributes
        # that you can access to
        # get information about each tweet
    list_tweets = [tweet for tweet in tweets]
 
    # Counter to maintain Tweet Count
    i = 1
 
    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
            id = tweet.id
            time = tweet.created_at
                 
            # Retweets can be distinguished by
            # a retweeted_status attribute,
            # in case it is an invalid reference,
            # except block will be executed
            try:
                    text = tweet.retweeted_status.full_text
            except AttributeError:
                    text = tweet.full_text
 
            # Here we are appending all the
            # extracted information in the DataFrame
            ith_tweet = [id, time, text]
            db.loc[len(db)] = ith_tweet
            
    return db
