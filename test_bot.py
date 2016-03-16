import tweepy, time, sys, wikiquote

def tweet():
    if len(quotes[0]) < 121:
        api.update_status(quotes[0])
    else:
        api.update_status("Rustybot Hungry!")


CONSUMER_KEY = 'YQNoFyZGGfumxlaEHBbhyhosb'
CONSUMER_SECRET = 'OslbErkHeoZJ0g6ANx8WewURwyXcIAC09AGihX8XRd7uLEEsp2'
ACCESS_KEY =  '709895920444243968-KOxIoRW2zk45cjUJ7dlRMlRNXQjMQld'
ACCESS_SECRET = '1QCnOtzr2FMjXk6sfkXzbjoeq3WR8nRT1lYnZ2ZPZkVBW'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


try:
    quotes = wikiquote.quotes("Albert Einstein")
except:
    pass


for each in quotes:
    if len(each) < 121:
        print(each)



    


