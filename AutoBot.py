#AutoBot.py
#Adam Vilmin
#2016-March- crappyoats@gmail.com

from Bot import *
from time import sleep

class AutoBot(Bot):
    """provides interface for running a rusty_bot in Auto Mode"""

    def __init__(self):
        super().__init__()

    def main_routine(self):
        """runs bot in auto mode"""
        self._pull_quotes()
        while(1):
            self.tweet()
            sleep(600)

    def _pull_quotes(self):
        """routine to mine quotes for rustybot"""
        searchs = ["physics", "probability", "chef"]

        while len(searchs) > 0:
            t = searchs.pop()
            topics = self.search_topic(t)

            for each in topics:
                self.add_topic(each)

        
