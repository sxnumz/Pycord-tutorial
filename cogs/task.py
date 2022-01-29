import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option, user_command, message_command
from datetime import time

class tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_member = 0
        self.looping.start()

    def cog_unload(self):
        self.looping.cancel()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @tasks.loop(minutes=30)
    # @tasks.loop(time=time(hour=15, minute=30)) # GMT time 
    async def looping(self):
        guild = self.bot.get_guild(SERVER_ID)
        total_member = guild.member_count
        if self.server_member != total_member:
            self.server_member = total_member
            channel = guild.get_channel(CHANNEL_ID)
            await channel.edit(name=f'Members - {self.server_member}')

        # channel = self.bot.get_channel(CHANNEL_ID)
        # await channel.send('TESTING LOOP')

    @looping.before_loop
    async def looping_before(self):
        await self.bot.wait_until_ready()
        print('Loop is ready!')

def setup(bot):
    bot.add_cog(tasks(bot))