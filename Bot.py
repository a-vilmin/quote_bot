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

    def _find_quotes(self, term):
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


            
    #class methods

    def search_topic(self, topic = "computer science"):
        """runs wikiquote search. adds search terms to topics list. default
        search term is 'computer science'. returns list of possible searches"""

        try:
            topics = wikiquote.search(topic)
            return topics
        except:
            pass


    def add_topic(self, topic):
            try:
                quotes = self._find_quotes(topic)
                self.__topics[topic] = quotes              
            except:
                pass        
    
    def tweet(self):
        """pull quote out and tweet it"""
        key = sample(list(self.__topics), 1)[0]
            
        end = len(self.__topics[key])
        index = randint(0, end-1)
            
        tweet = self.__topics[key].pop(index)
        print(tweet)
        self.__api.update_status(tweet)
    
        
if __name__ == '__main__':
    new_bot = Bot()
    topics = new_bot.search_topic()

    for each in topics:
        new_bot.add_topic(each)
        
    new_bot.tweet()

    


