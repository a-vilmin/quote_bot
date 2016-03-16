from Bot import *
fromt time import sleep

class AutoBot():
    """provides interface for running a rusty_bot in Auto Mode"""

    def __init__(self):
        self.__bot = Bot()

    def main_routine(self):
        """runs bot in auto mode"""
        topics = self.__bot.search_topic()

        for each in topics:
            self.__bot.add_topic(topics)

        while(1):
            new_bot.tweet()
            sleep(300)
