from Bot import *
from time import sleep

class AutoBot():
    """provides interface for running a rusty_bot in Auto Mode"""

    def __init__(self):
        self.__bot = Bot()

    def main_routine(self):
        """runs bot in auto mode"""
        topics = self.__bot.search_topic()

        for each in topics:
            self.__bot.add_topic(each)

        while(1):
            self.__bot.tweet()
            sleep(300)
