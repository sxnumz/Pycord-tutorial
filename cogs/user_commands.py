import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command

class user_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @user_command(guild_ids=[SERVER_ID])
    async def avatar(self, ctx, member:discord.Member):
        embed = discord.Embed()
        if member.avatar is not None:
            embed.set_image(url=member.avatar)
            return await ctx.respond(embed=embed)
        await ctx.respond("This user don't hava a avatar", ephemeral=True)
    
    @user_command(guild_ids=[SERVER_ID])
    async def banner(self, ctx, member:discord.Member):
        fetch_member = await self.bot.fetch_user(member.id)

        embed = discord.Embed()
        if fetch_member.banner is not None:
            embed.set_image(url=fetch_member.banner)
            return await ctx.respond(embed=embed)
        await ctx.respond("This user don't hava a banner", ephemeral=True)

def setup(bot):
    bot.add_cog(user_commands(bot))