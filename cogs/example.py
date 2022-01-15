import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[SERVER_ID])
    async def hello_slash(self, ctx):
        await ctx.respond('hello slash')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello')

def setup(bot):
    bot.add_cog(example(bot))