import discord
from discord.ext import commands
import asyncio
import praw
import random
import builtins

botPrefix = "cursed"
client = commands.Bot(command_prefix = botPrefix)
builtins.client = client
client.remove_command("help")

@client.event
async def on_server_join(server):
    pass

@client.event
async def on_ready():
    pass

import personal
import pizza
import reddit

client.run()