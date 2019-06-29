from builtins import client
from PIL import Image, ImageEnhance
from io import BytesIO
import requests, os
from os import path

basePath = path.dirname(__file__)

@client.command(pass_context = True)
async def cursecam(ctx):
    args = ctx.message.content.replace("//cursecam ", "").replace("<", "").replace("@", "").replace("!", "").replace(">", "")
    #takes the content of the message and removes the base command, and if you tag someone, it removes everything except the user id
    if args == "//cursecam":
        args = ctx.message.author.id
        #if the person didn't tag anyone, it'd just take their user id
    try:
        removeStr = int(args)
        #primalrages the string to see if it can converted to a string, if the message is "//curseme hi", then it'd except the error
        cursedUser = await client.get_user_info(args)
        #grabs the user info using the user id
    except:
        await client.say("That's not a valid user.")
        return
    requestedImg = requests.get(cursedUser.avatar_url)
    img = Image.open(BytesIO(requestedImg.content))
    #grabs their profile picture information and opens it using PIL so I can edit it
    img = img.resize((512, 512))
    #resizes the image to fit better
    filePath = path.abspath(path.join(basePath, "Other Files", "cursecamfilter.png"))
    overlay = Image.open(filePath)
    img.paste(overlay, (0, 0, 512, 512), overlay)
    #opens the cursed filter and sets it on top of the profile picture
    tempPath = path.abspath(path.join(basePath, "Other Files", "cursecam.png"))
    img.save(tempPath, format = "PNG")
    await client.send_file(ctx.message.channel, tempPath)
    os.remove(tempPath)
    #temporarily saves the file, posts it, and then removes it

@client.command(pass_context = True)
async def curseme(ctx):
    args = ctx.message.content.replace("//curseme ", "").replace("<", "").replace("@", "").replace("!", "").replace(">",
                                                                                                                    "")
    if args == "//curseme":
        args = ctx.message.author.id
    try:
        removeStr = int(args)
        cursedUser = await client.get_user_info(args)
    except:
        await client.say("That's not a valid user.")
        return
    requestedImg = requests.get(cursedUser.avatar_url)
    img = Image.open(BytesIO(requestedImg.content)).resize((512, 512)).convert("RGB")
    img = ImageEnhance.Sharpness(img)
    filePath = path.abspath(path.join(basePath, "Other Files", "curseme.png"))
    img.enhance(1000000000000).save(filePath, format = "JPEG", quality = 1)
    #you grab the pfp just like before, but then you sharpen it by a billion times
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    img = Image.open(filePath)
    img.save(filePath, format = "JPEG", quality = 1)
    #and you jpeg blast it to hecc and back
    await client.send_file(ctx.message.channel, filePath)
    os.remove(filePath)

@client.command(pass_context = True)
async def primalrage(ctx):
    args = ctx.message.content.replace("//primalrage ", "").replace("<", "").replace("@", "").replace("!", "").replace(">",
                                                                                                                    "")
    if args == "//primalrage":
        args = ctx.message.author.id
    try:
        removeStr = int(args)
        cursedUser = await client.get_user_info(args)
    except:
        await client.say("That's not a valid user.")
        return
    requestedImg = requests.get(cursedUser.avatar_url)
    img = Image.open(BytesIO(requestedImg.content))
    img = img.resize((512, 512))
    filePath = path.abspath(path.join(basePath, "Other Files", "primalragefilter.png"))
    overlay = Image.open(filePath)
    img.paste(overlay, (0, 0, 512, 512), overlay)
    tempPath = path.abspath(path.join(basePath, "Other Files", "primalrage.png"))
    img.save(tempPath, format = "PNG")
    await client.send_file(ctx.message.channel, tempPath)
    os.remove(tempPath)

@client.command(pass_context = True)
async def static(ctx):
    args = ctx.message.content.replace("//static ", "").replace("<", "").replace("@", "").replace("!", "").replace(">",
                                                                                                                    "")
    if args == "//static":
        args = ctx.message.author.id
    try:
        removeStr = int(args)
        cursedUser = await client.get_user_info(args)
    except:
        await client.say("That's not a valid user.")
        return
    requestedImg = requests.get(cursedUser.avatar_url)
    img = Image.open(BytesIO(requestedImg.content))
    img = img.resize((512, 512))
    filePath = path.abspath(path.join(basePath, "Other Files", "staticfilter.png"))
    overlay = Image.open(filePath)
    img.paste(overlay, (0, 0, 512, 512), overlay)
    tempPath = path.abspath(path.join(basePath, "Other Files", "static.png"))
    img.save(tempPath, format = "PNG")
    await client.send_file(ctx.message.channel, tempPath)
    os.remove(tempPath)
#the above two are the same as cursecam, but with different filters