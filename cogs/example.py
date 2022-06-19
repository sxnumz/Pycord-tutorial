import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[986665524924661850])
    async def hello_slash(self, ctx):
        embed = discord.Embed(color=0xB983FF, timestamp=discord.utils.utcnow())

        embed.title = 'Script'
        embed.description = 'tutorial pycord\nep1.5'
        embed.add_field(name='field1', value='text', inline=True)
        embed.add_field(name='field2', value='text', inline=True)
        embed.add_field(name='field3', value='text', inline=False)

        embed.set_image(url='https://i.imgur.com/iYctNz2.png')
        embed.set_thumbnail(url='https://i.imgur.com/iYctNz2.png')

        embed.set_footer(text='footer', icon_url='https://i.imgur.com/iYctNz2.png')

        embed.set_author(name='author', icon_url='https://i.imgur.com/iYctNz2.png', url='https://i.imgur.com/iYctNz2.png')

        await ctx.respond(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello')

def setup(bot):
    bot.add_cog(example(bot))
