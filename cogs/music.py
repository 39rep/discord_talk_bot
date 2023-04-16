import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp

import settings


class MusicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] MusicCog is ready.")

    # @commands.hybrid_command(name="ping",)
    # # @app_commands.guilds(int(settings.getId()))
    # async def ping(self, ctx:commands.Context, text: str):
    #     await ctx.send('pong')
        
async def setup(bot: commands.Bot):
    await bot.add_cog(MusicCog(bot))