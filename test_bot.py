from sys import argv
import tweepy, wikiquote

class Bot():

    def __init__(self):
        """initialize bot with app api"""
        self.__api = self._twitter_init()
        self.__topics = []

    #helper methods/getter/setter
    
    def _twitter_init(self):
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

    def _set_topics(self, topics):
        if len(self.__topics) == 0:
            self.__topics = topics
        else:
            self.__topics += topics
            
    #class methods

    def search_topic(self, topic = "computer science"):
        """runs wikiquote search. adds search terms to topics list. default
        search term is 'computer science'"""

        try:
            topics = wikipedia.search(topic)
            self._set_topics(topics)
        except:
            pass
                
        

if __name__ == '__main__':
    new_bot = Bot()
    new_bot.search_topic()



    


