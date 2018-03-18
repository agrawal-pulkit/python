

import sys

import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

class TweetsListener(StreamListener):
    
    def __init__(self):
        print('Tweet Listener class initialized.')
    
    def on_data(self, data):
        print("on_data: {0}".format(data))
        return True
    
    def on_error(self, status):
        print("error: {0}".format(status))
        return True


if __name__ == "__main__":

    api_key = "05vmjOLTZazXj2doCsLYPXMgx"
    api_secret = "OxV7iOFKA3x3nBBF9WHSpQ0w1SVcNdEjOt3GZPmFqDszahb31L"
    
    access_token = "1427298992-FNne49AJM0fnq6ZiHBB7RcjcxsslFwLD7Uj4Pnj"
    access_token_secret = "7V4RDqhgxaemcb42mbBIY50T6eSYDesN6TzMcrxZKohww"
    
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    twitter_stream = Stream(auth, TweetsListener())
    twitter_stream.filter(track=["#"])