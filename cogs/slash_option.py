import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class slash_example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="My infomation", guild_ids=[SERVER_ID])
    async def myinfo(
        self,
        ctx,
        name: Option(str, 'Enter you name'),
        gender: Option(str, 'Choose your gender', choices=['Male','Female','Other']),
        age: Option(int, 'Enter your age', required=False, default=15)
    ):  
        # Text  = str
        # Number = int
        
        await ctx.respond(f'Name: {name}\nGender: {gender}\nAge: {age}')

    @slash_command(description="member commands", guild_ids=[SERVER_ID])
    async def member(
        self,
        ctx,
        member: Option(discord.Member, 'Spectify Member')
    ):  
        # Member = discord.Member
        # User =  discord.User

        await ctx.respond(member)

    @slash_command(description="channel commands", guild_ids=[SERVER_ID])
    async def channel(
        self,
        ctx,
        channel: Option(discord.TextChannel, description='Spectify channel')
    ):  
        # Voice = discord.VoiceChannel
        # Text = discord.TextChannel
        # Stage = discord.StageChannel
        # Thread = discord.Thread

        await ctx.respond(channel)
    
    #prive_message
    @slash_command(guild_ids=[SERVER_ID])
    async def hihi(self, ctx):
        await ctx.respond('hi hi', ephemeral=True)

def setup(bot):
    bot.add_cog(slash_example(bot))