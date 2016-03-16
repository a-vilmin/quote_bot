from sys import argv
import tweepy, wikiquote

class Bot():

    def __init__(self):
        """initialize bot with app api"""
        self.__api = self._twitter_init()
        self.__topics = {}
        
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

    def _add_topics(self, topics):
        for each in topics:
            try:
                if not self.__topics[each]:
                    self.__topics[each] = []
            except:
                pass
            
    #class methods

    def search_topic(self, topic = "computer science"):
        """runs wikiquote search. adds search terms to topics list. default
        search term is 'computer science'"""

        try:
            topics = wikipedia.search(topic)
            self._add_topics(topics)
        except:
            pass

    def find_quotes(self):
        """find quotes for search terms in topic dict. filters for less than 
        120 characters"""

        for key, value in self.__topics:
            try:
                if not value:
                    quotes = wikiquote.quotes(key)

                    for each in quotes:
                        if len(each) < 121:
                            self.__topics[key] += [each]
            except:
                pass
            
        

if __name__ == '__main__':
    new_bot = Bot()
    new_bot.search_topic()



    


