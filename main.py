import os
import difflib
import sqlite3
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
import os
from discord_webhook import DiscordWebhook
import time
import random
client = commands.Bot(command_prefix='.')
client2 = commands.Bot(command_prefix='.')
#to add more add client3 = commands.Bot(command_prefix='.') and so one from 3

@client.command()
async def ping(ctx):
  await ctx.send('pong')
  
  





  
  
        







keep_alive()
loop = asyncio.get_event_loop()
loop.create_task(client.start(os.getenv("TOKEN"),bot=False))
loop.create_task(client2.start(os.getenv("TOKEN1"),bot=False))
loop.run_forever()
#to add more add loop.create_task(client3.start(os.getenv("TOKEN1"),bot=False)) and so on from 3
