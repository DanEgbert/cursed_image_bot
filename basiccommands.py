import discord
from builtins import client
import random, os
from os import path

basePath = path.dirname(__file__)

@client.command(pass_context = True)
async def cursedpizza(ctx):
    filePath = path.abspath(path.join(basePath, "Other Files", "cursedpizza.txt"))
    cursePizzaFile = open(filePath, "r")
    #I used the console in chrome to grab a bunch of urls of cursed pizza, put it in a text file, and then opens the file in read mode
    #this also has the unintended effect of sometimes grabbing normal pizzas, but I find that funnier because of the caption that comes with every image
    cPUrl = random.choice(cursePizzaFile.read().split("\n"))
    #splits the file into a list using newline, and picks a url at random
    badColors = random.choice([0x69942, 0x597146, 0x3d6d18, 0x5e6d18, 0x3c4419, 0x284419, 0x556b4a, 0x064331, 0x366154, 0x3c6136])
    try:
        em = discord.Embed(title = "What an abomination.", color = badColors)
        em.set_image(url = cPUrl)
        await client.send_message(ctx.message.channel, embed = em)
        #creates an embed with the picture of the pizza, and a message informing everyone of the horror they're about to see
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))

@client.command(pass_context = True)
async def help(ctx):
    badColors = random.choice([0x69942, 0x597146, 0x3d6d18, 0x5e6d18, 0x3c4419, 0x284419, 0x556b4a, 0x064331, 0x366154, 0x3c6136])
    #randomly selects a set of bad/gross colors I've picked out
    em = discord.Embed(title = "Cursed Bot Help", url = "https://cdn.discordapp.com/avatars/592767520449232906/911c4c0ced706d76048d420730043e08.webp?size=1024", description = "A quick menu to look at the different commands this cursed bot has.", color = badColors)
    em.set_author(name = ctx.message.author.name, url = ctx.message.author.avatar_url, icon_url = ctx.message.author.avatar_url)
    em.set_thumbnail(url = "https://cdn.discordapp.com/avatars/592767520449232906/911c4c0ced706d76048d420730043e08.webp?size=1024")
    em.add_field(name = "//cursecam", value = "You're in the nightmares of every security officer everywhere.")
    em.add_field(name = "//cursedcomments", value = "Chooses a random image from r/cursedcomments.")
    em.add_field(name = "//cursedcursedcomments", value = "Chooses a random image from r/cursedcursedcomments.")
    em.add_field(name = "//cursedfoods", value = "Chooses a random image from r/cursedfoods.")
    em.add_field(name = "//cursedimages", value = "Chooses a random image from r/cursedimages.")
    em.add_field(name = "//cursedminecraft", value = "Chooses a random image from r/cursedminecraft.")
    em.add_field(name = "//cursedpizza",value = "Selects a top Google Image search result to show you the most cursed of all pizza.")
    em.add_field(name = "//curseme", value = "This makes your profile picture cursed.")
    em.add_field(name = "//help", value = "The command you're currently looking at!")
    em.add_field(name = "//personalpick", value = "Some of our personal picks for best cursed images.")
    em.add_field(name = "//primalrage", value = "Release your inner rage, leave no one alive.")
    em.add_field(name = "//static", value = "Huh? I can't quite see your profile picture. Are you sure the reception here is good?")
    em.set_footer(text = "You have been cursed already, please don't try to get cursed further.")
    #creates an embed with all the commands and a description of what they do, with small additions like having the bot's avatar as the thumbnail, and the author info, the footer, etc.
    await client.send_message(ctx.message.channel, embed = em)

@client.command(pass_context = True)
async def personalpick(ctx):
    filePath = path.abspath(path.join(basePath, "Personal Cursed Images"))
    imgFile = random.choice(os.listdir(filePath))
    imgPath = filePath + "/{0}".format(imgFile)
    #takes all the files in the folder and makes each one part of a list
    #it then picks a random one, and adds it to a string that's the filepath of that image
    await client.send_file(ctx.message.channel, imgPath, filename = "personalpick.png", content = "Enjoy this personal favorite!")
    #it then sends the file of our personal pick to the channel