

import sys
import pprint
import socket
import json

import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

class TweetsListener(StreamListener):
    
    def __init__(self, socket):
        self.client_socket = socket
        print('Tweet Listener class initialized.')
    
    def on_data(self, data):
        try:
            jsonMessage = json.loads(data)
            message = jsonMessage['text'].encode('utf-8')
            print("message: {0}".format(message))
            self.client_socket.send(message)
        except BaseException as e:
            print("Error on_data: {0}".format(e))
        return True
    
    def on_error(self, status):
        print("error: {0}".format(status))
        return True
    
def connect_to_twitter(connection):
    api_key = "05vmjOLTZazXj2doCsLYPXMgx"
    api_secret = "OxV7iOFKA3x3nBBF9WHSpQ0w1SVcNdEjOt3GZPmFqDszahb31L"
    
    access_token = "1427298992-FNne49AJM0fnq6ZiHBB7RcjcxsslFwLD7Uj4Pnj"
    access_token_secret = "7V4RDqhgxaemcb42mbBIY50T6eSYDesN6TzMcrxZKohww"
    
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    twitter_stream = Stream(auth, TweetsListener(connection))
    twitter_stream.filter(track=["#"])

if __name__ == "__main__":
    
    s = socket.socket()
    host = "localhost"
    port = 7777
    s.bind((host, port))
    
    print("listening on port: {0}".format(port))
    
    s.listen(5)
    
    connection, client_address = s.accept()
    
    print("Recivied request from: {0}".format(client_address))
    
    connect_to_twitter(connection)
