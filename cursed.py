from discord.ext import commands
import builtins
from config import botToken
#importing the bot token from a config file

botPrefix = "//"
client = commands.Bot(command_prefix = botPrefix)
builtins.client = client
client.remove_command("help")
#setting the prefix to '//', and then removing the help command to implement a custom one

@client.event
async def on_ready():
    print("Hackerman.")
    #it's hack week, so I'm hackerman

@client.event
async def on_server_join(server):
    for channel in server.channels:
        if str(channel.type) == "text" and channel.permissions_for(server.me).send_messages:
            await client.send_message(channel, "Your eyes will never be the same, prepare to die from all the curses you will receive. My prefix is ``//``!")
            #just a message that gets posted in the first channel that the bot can post in when it joins a server, so right off the bat people know the prefix
            break

import basiccommands
import cursefilter
import reddit
#importing all the other files with the commands in them, to keep the main file cleaner

client.run(botToken)