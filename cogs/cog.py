from discord.ext import commands
from wrapper import db
import asyncio

class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def create_db(self, ctx):
    v = await ctx.send("Creating database")
    db.create_db(ctx.guild.id)
    await v.edit(content=f"Your database has been created!\nPS: {ctx.guild.id} is your database")

  @commands.command()
  #@commands.has_permission("manage_guild")
  async def delete_db(self, ctx):
    f"""delete {ctx.guild.name}'s database'"""
    
    message = await ctx.send(f"Are you sure you want to delete your database?")
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel

    try:
        confirm = await self.bot.wait_for("message", check=check, timeout=30)

    except asyncio.TimeoutError:
        await message.edit(content="Prompt canceled, Time out")
        return

    if confirm.content == "yes":
      db.delete_db(ctx.guild.id)
      return await message.edit(content="Deleted your database.")

    await message.edit(content="Deletion canceled")

  @commands.command()
  async def store(self, ctx, arg1, arg2):
    a = await ctx.reply(f"Constructing your query\n```{arg1} : {arg2}```")
    db.store(arg1, arg2, ctx.guild.id)
    await a.edit(content="Query made sending! :cloud:")
  
  @commands.command()
  async def get(self, ctx, arg1):
    a = await ctx.reply(f"Constructing your query\n```{arg1} : [???]```")
    b = await a.edit(content=db.key_focus(arg1, '4162'))
    await b.edit(f"{db.key_focus(arg1, ctx.guild.id)}")
  


def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')