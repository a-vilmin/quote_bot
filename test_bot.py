from sys import argv
from random import sample, randint
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
        with open(filename) as f:
            content = [x.strip('\n') for x in f.readlines()]

        CONSUMER_KEY = content[0]
        CONSUMER_SECRET = content[1]
        ACCESS_KEY = content[2]
        ACCESS_SECRET = content[3]

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        return tweepy.API(auth)

    def _add_topics(self, topics):
        for each in topics:
            try:
                quotes = self.find_quotes(each)
                self.__topics[each] = quotes              
            except:
                pass
            
    #class methods

    def search_topic(self, topic = "computer science"):
        """runs wikiquote search. adds search terms to topics list. default
        search term is 'computer science'"""

        try:
            topics = wikiquote.search(topic)
            self._add_topics(topics)
        except:
            pass

    def find_quotes(self, term):
        """find quotes for search terms in topic dict. filters for less than 
        120 characters"""
        try:
            tweetable = []
            quotes = wikiquote.quotes(term)
            for each in quotes:
                if len(each) < 121:
                    tweetable += [each]

            return tweetable
        except:
            pass                    

    def tweet(self):
        """pull quote out and tweet it"""
        key = sample(list(self.__topics), 1)[0]

        end = len(self.__topics[key])
        index = randint(0, end-1)

        tweet = self.__topics[key][index]

        self.__api.update_status(tweet)

if __name__ == '__main__':
    new_bot = Bot()
    new_bot.search_topic()
    new_bot.tweet()

    


