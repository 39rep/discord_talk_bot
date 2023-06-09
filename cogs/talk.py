import discord
from discord.ext import commands
from discord import app_commands

from models import gpt
import settings

arona_gpt = gpt.Gpt(settings.getKey())

class TalkCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] TalkCog is ready.")

    @commands.hybrid_command(
        name="talk",
        description="アロナとお話ができます。"
    )
    @app_commands.guilds(int(settings.getId()))
    async def talk(self, ctx:commands.Context, text: str):
        if ctx.channel.name == 'talk-with-arona':
            await ctx.defer()
            try:
                message = arona_gpt.completion(text)
            except Exception as e:
                message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
                print(e)
            # embed=discord.Embed(title=text, description=message, color=0x39C7EC)
            await ctx.send(message)
        else:
            await ctx.send('指定されたチャンネル名と一致しません。')
        
async def setup(bot: commands.Bot):
    await bot.add_cog(TalkCog(bot))