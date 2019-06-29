import discord
from builtins import client
import random
from config import reddit
#importing the variable 'reddit' from the config file, it has all the login info for PRAW

badColors = random.choice([0x69942, 0x597146, 0x3d6d18, 0x5e6d18, 0x3c4419, 0x284419, 0x556b4a, 0x064331, 0x366154, 0x3c6136])

@client.command(pass_context = True)
async def cursedcomments(ctx):
    sub = reddit.subreddit('cursedcomments')
    post = sub.random()
    #the sub variable grabs the subreddit, and then post grabs a random post from that subreddit
    try:
        em = discord.Embed(title = post.title, url = "https://www.reddit.com{0}".format(post.permalink), color = badColors)
        em.set_image(url = post.url)
        em.set_footer(text = "👌 {0} | 👄 {1}".format(post.score, post.num_comments))
        await client.send_message(ctx.message.channel, embed = em)
        #creates an embed with the information from the post, with ok hand being upvotes, and lips being comments, since those seemed more cursed to me
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))
        #when an error occurs, it says what the error is. This is mostly added because of an http error that happens sometimes

@client.command(pass_context = True)
async def cursedcursedcomments(ctx):
    sub = reddit.subreddit('cursedcursedcomments')
    post = sub.random()
    try:
        em = discord.Embed(title = post.title, url = "https://www.reddit.com{0}".format(post.permalink), color = badColors)
        em.set_image(url = post.url)
        em.set_footer(text = "👌 {0} | 👄 {1}".format(post.score, post.num_comments))
        await client.send_message(ctx.message.channel, embed = em)
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))
    #the same as above, but for a different subreddit

@client.command(pass_context = True)
async def cursedfoods(ctx):
    sub = reddit.subreddit('cursedfoods')
    post = sub.random()
    try:
        em = discord.Embed(title = post.title, url = "https://www.reddit.com{0}".format(post.permalink), color = badColors)
        em.set_image(url = post.url)
        em.set_footer(text = "👌 {0} | 👄 {1}".format(post.score, post.num_comments))
        await client.send_message(ctx.message.channel, embed = em)
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))


@client.command(pass_context = True)
async def cursedimages(ctx):
    sub = reddit.subreddit('cursedimages')
    post = sub.random()
    try:
        em = discord.Embed(title = post.title, url = "https://www.reddit.com{0}".format(post.permalink), color = badColors)
        em.set_image(url = post.url)
        em.set_footer(text = "👌 {0} | 👄 {1}".format(post.score, post.num_comments))
        await client.send_message(ctx.message.channel, embed = em)
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))

@client.command(pass_context = True)
async def cursedminecraft(ctx):
    sub = reddit.subreddit('cursedminecraft')
    post = sub.random()
    try:
        em = discord.Embed(title = post.title, url = "https://www.reddit.com{0}".format(post.permalink), color = badColors)
        em.set_image(url = post.url)
        em.set_footer(text = "👌 {0} | 👄 {1}".format(post.score, post.num_comments))
        await client.send_message(ctx.message.channel, embed = em)
    except Exception as e:
        await client.say("An error has occurred. The error is:\n{0}".format(e))
#same with all these