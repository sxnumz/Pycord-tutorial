import discord
from discord.ext import commands
from discord.commands import slash_command, permissions

# สามารถเพิ่ม permissions ต่อคำสั่งมากสุด 10 อย่าง
# @permissions.is_user(user_id)
# @permissions.is_owner(guild_id)
# @permissions.has_role(role_id / role_name)
# @permissions.has_any_role(role_id / role_name)
# @permissions.permission(user_id, role_id, guild_id)
# @slash_command(
#         default_permission=False,
#         permissions=[permissions.CommandPermission(id=ID, type=TYPE, permission=True, guild_id=GUILD_ID)]
#     )

# ใส่ GUILD_ID กับ USER_ID ตรงนี้ได้เลยนะครับ

GUILD_ID = []
USER_ID = ...

class slash_perm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[GUILD_ID], default_permission=False)
    @permissions.is_user(USER_ID)
    async def user(self, ctx):
        await ctx.respond("only you")
    
    @slash_command(guild_ids=[GUILD_ID], default_permission=False)
    @permissions.is_owner()
    async def owner(self, ctx):
        await ctx.respond("owner")

    @slash_command(guild_ids=[GUILD_ID], default_permission=False)
    # @permissions.has_role("⠀ROLE NAME")
    @permissions.has_role(USER_ID)
    async def role(self, ctx):
        await ctx.respond("role")
    
    @slash_command(guild_ids=[GUILD_ID], default_permission=False)
    @permissions.has_any_role(ROLE_NAME, ROLE_ID)
    async def role2(self, ctx):
        await ctx.respond("role 2")

    @slash_command(guild_ids=GUILD_ID, default_permission=False)
    @permissions.permission(user_id=USER_ID, role_id=role_id, guild_id=guild_id) # ใส่แยกจากตัวบนนะครับ มันใส่ได้แค่อันเดียว
    async def multi(self, ctx):
        await ctx.respond("multi")

    @slash_command(
        guild_ids=GUILD_ID,
        default_permission=False,
        permissions=[permissions.CommandPermission(id=USER_ID, type=2, permission=True)]
    )
    async def permission_kwarg(self, ctx):
        await ctx.respond("permission_kwarg")

def setup(bot):
    bot.add_cog(slash_perm(bot))