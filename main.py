import nextcord #DO NOT REMOVE
import os #DO NOT REMOVE
# import json
# import time
from keep_alive import keep_alive
from nextcord.ext import commands #DO NOT REMOVE
#Common imports for various features
# import aiosqlite
import logging

# from replit import db

logging.basicConfig(level=logging.INFO)

intents = nextcord.Intents.default()
intents.members = True
#To gather server members from whatever server the bot is in
#REQUIRES ENABLING "SERVER MEMBER INTENT" FROM THE discord DEVELOPER PORTAL

bot = commands.Bot(command_prefix = "!") #Change the prefix however you'd like

@bot.command()
async def load(ctx,extension):
  bot.load_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been loaded")

@bot.command()
async def unload(ctx,extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been unloaded")

@bot.command(aliases=['r'])
async def reload(ctx,extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been unloaded")
  bot.load_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been reloaded")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
#Loads every file in the cogs folder
#This will add the .py extension for you so do not do it yourself in the cogs table

@bot.event
async def on_ready():
  await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="any Humans."))
  print(f"{bot.user} is online!") #Checks when the bot is online and prints it to the console

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Sorry, you wont be able to check in again for another  %.2fs. Yes... that is correct, seconds...why not convert to minuites you ask?? Well, maths thats why :)' % error.retry_after)
    raise error

keep_alive()
bot.run(os.getenv("TOKEN")) #Runs the bot, I suggest NOT pasting your token in the string which is why I used the os import to get it through a SECRET TOKEN (Read the README.md for more info)

#If people get access to your token they can and probably will run yout bot with their code instead so ALWAYS USE ENV VARIABLES
