from discord.ext import commands
import os
from dotenv import load_dotenv
import bot_controller
from bot_controller import *


class MyBot(commands.Bot):

    def __init__(self, command_prefix, self_bot):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
        self.message1 = "[INFO]: Bot now online"
        self.message2 = "Bot still online"
        self.add_commands()

    async def on_ready(self):
        print(self.message1)

    def add_commands(self):
        @self.command(name="status", pass_context=True)
        async def status(ctx):
            print(ctx)
            await ctx.channel.send(self.message2, ctx.author.name)

        self.add_command(status)


load_dotenv()
bot = MyBot(command_prefix="!", self_bot=False)
bot.run(os.getenv("TOKEN"))
