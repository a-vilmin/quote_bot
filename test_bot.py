import tweepy, time, sys, wikiquote


class bot():

    def __init__():
        """initialize bot with app api"""
        self.__api = self._twitter_init()





    def _twitter_init():
        """helper method for init bot"""
        filename = argv[1]
        txt = open(filename)

        CONSUMER_KEY = filename[0]
        CONSUMER_SECRET = filename[1]
        ACCESS_KEY = filename[2]
        ACCESS_SECRET = filename[3]

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        return tweepy.API(auth)


        



    


