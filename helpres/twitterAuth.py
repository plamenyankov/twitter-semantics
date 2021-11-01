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
        return self.api

    '''Search for a keyword from a date'''
    def search(self, search_words, date_from):
        # self.api.user_timeline(screen_name = screen_name,count=200, tweet_mode="extended")
        tweets = tw.Cursor(self.api.search_tweets,
                       q=search_words,
                       lang="en",
                    #    geocode="34.052235,-118.243683,100km",
                       since=date_from).items(1)
        
        return tweets               
    

