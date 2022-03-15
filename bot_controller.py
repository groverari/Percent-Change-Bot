import bot
from bot import *


class BotController:
    @staticmethod
    def add_stock(username, stock_name):
        print("bot control")
        bot.send_message(username, "hello")

    def push_stock(self):
        pass

    def watch_stocks(self):
        pass
