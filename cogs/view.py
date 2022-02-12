import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command


class MyView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__(timeout=10)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("you can't do this", ephemeral=True)
        return False
    
    async def on_timeout(self):
        if self.message:
            # self.button_1.disabled = True
            # self.myselect.disabled = True
            await self.message.edit_original_message(view=None)
        
    @discord.ui.button(label="Button 1", style=discord.ButtonStyle.blurple, row=1)
    async def button_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"{self.ctx.author}", ephemeral=True)

    @discord.ui.select(placeholder="Selection. . .", row=0, options=[
        discord.SelectOption(label="stacia", description="this is my name", emoji='⭐'),
        discord.SelectOption(label="renly", description="my 2nd name", emoji='<:ExclusiveRarity:941530500470800445>'),
    ])
    async def myselect(self, select: discord.ui.Select, interaction: discord.Interaction):
        if select.values[0] == "stacia":
            await interaction.response.send_message("choice 1", ephemeral=True)
        elif select.values[0] == "renly":
            await interaction.response.send_message("choice 2", ephemeral=True)

class view_tutorial(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[931480707040174100])
    async def buttonview(self, ctx):

        view = MyView(ctx)
        view.message = await ctx.respond("VIEW TEST", view=view)
    
def setup(bot):
    bot.add_cog(view_tutorial(bot))