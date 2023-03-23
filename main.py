import time

import settings
import discord
from discord.ext import commands

# intents設定しないとBOTが応答しない
intents = discord.Intents.all()
intents.message_content = True

INITAL_EXTENSIONS = [
    "cogs.talk",
]

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('.'),
            # activity=discord.Game(name='>------- Now loading -------<'),
            # status=discord.Status.idle,
            activity=discord.Game(name='いんたーねっと'),
            status=discord.Status.online,
            case_insensitive=True,
            help_command=None,
            intents=intents
        )
    
    async def setup_hook(self):
        for extension in INITAL_EXTENSIONS:
            await self.load_extension(extension)

if __name__ == '__main__':
    bot_token = settings.getToken()
    print(f'bot token: {bot_token}')
    MyBot().run(bot_token)
