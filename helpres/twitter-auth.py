# Twitter class for Authotication of user
import tweepy as tw

class Twitter:

    def __init__(self, ck, cs, at, ats, b):
        self.consumer_key = ck
        self.consumer_secret = cs
        self.access_token = at
        self.access_token_secret = ats
        self.bearer = b
        self.connect()

    '''Connect to Twitter API'''
    def connect(self):
        auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True)    
        

    '''Search for a keyword from a date'''
    def search(self, search_words, date_from):
        tweets = tw.Cursor(self.api.search_tweets,
                       q=search_words,
                       lang="en",
                       since=date_from).items(5)
        return tweets               
    

