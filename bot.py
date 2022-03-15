import discord
import os
from dotenv import load_dotenv
import bot_controller
from bot_controller import *



class bot:

    def __init__(self):
        load_dotenv()
        self.client = discord.Client()
        self.client.run(os.getenv('TOKEN'))

    @client.event
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))


    @client.event
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('$add '):
            await message.channel.send("hello")
            #BotController.add_stock(message.author.id, message.content)


    def send_message(username, message):
        message.channel.send(f"<@{username} hello")



