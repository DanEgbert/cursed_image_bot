# cursed_image_bot

My entry to Hack Week for Discord.

## requirements/instructions for installing the bot
(This is mostly for other people if they want to recreate it, not for Discord staff team themselves, since they probably don't have time to recreate every bot for judging, and they would know most of it anyway. This is more of a beginner's guide.)
- Open windows powershell, and since this bot uses the async branch, instead of the rewrite branch, you'll have to type ``pip install discord.py==0.16.12``
- Install PIL
- Install PRAW
- Download the repository files
- Create a new Python file called 'config.py'
- In this config file, you first have to import PRAW, then you have to have to add two variables. One of them is called botToken, and you have to put the token for your bot in it.
- The other is called reddit, and for this variable you have to put in login information from a bot reddit account.
- To create one go to https://old.reddit.com/prefs/apps/, and if you aren't logged, log in/create a new account.
- Click create new app/create another app or whatever the button is, and then put whatever you want for the name, descriptions, and urls, but for the multiple choice one, you have to click 'script.'
- When you finish creating it, and click 'create app,' you'll then see your application pop up.
- Go back to the reddit variable that's empty, it should be set up like this:
```
reddit = praw.Reddit(client_id = "client_id", client_secret = "secret", username = "username", password = "your_password", user_agent = "this doesn't matter")
```
- For client id, check under the application name on the reddit apps page, right under 'personal use script', there should be a random string of characters, like "DA0eab5Pjay-Mf" or something.
- For client secret, it's right next to where it says secret on the page, self explanatory.
- For username and password, just use the username and password for the reddit account you're using.
- The user agent doesn't matter one bit, you can put anything there, but it's required for some reason.
After all this is finished, just run cursed.py as you would normally. Alternatively, you can add/remove pictures in /Personal Cursed Images/ since it is meant to be a personal pick.

## bot overview
I'm going to start with just the help command, but then just do the rest alphabetically.
###### //help
It just tells you every single command and a short description for each one, some more of a joke than others.
###### /cursecam
It grabs your profile picture, and then applies a filter on it, one that makes it look like the 'picture' got took with a night vision camera, that's also grainy.
###### //cursedcomments
It grabs a random post from the reddit r/cursedcomments.
###### //cursedcursedcomments
It grabs a random post from the reddit r/cursedcursedcomments.
###### //cursedfoods
It grabs a random post from the reddit r/cursedfoods, which is actually a subreddit made for the Youtube channel Shayy, or better known by his main channel as MattShea.
###### //cursedimages
It grabs a random post from the reddit r/cursedimages.
###### //cursedminecraft
It grabs a random post from the reddit r/cursedminecraft.
###### //cursedpizza
I took the top Google image search results for 'Brazilian pizza' and the bot shows a random one.
###### //curseme
It sharpens the image by 1 billion times, then jpg blasts it at 1 quality several times over.
###### //personalpick
It picks a random image from the /Personal Cursed Images/ folder, every single image there was hand picked by the other team member.
###### //primalrage
It adds a red filter on the profile picture that gets darker around the edges, making it look like the target in the middle is angrier.
###### //static
It adds a filter that greys out the profile picture, and adds a static effect.

One final note, not sure if Discord has access to my date of birth, but it is unironically my birthday on the 28th, which I find amusing. It was really fun making this bot, an enjoyable past time trying to do something new. I also learned a ton about PIL, and other stuff I've never used before. I've cut out a lot of stuff from the bot as I was making it, and I'll probably add it to the bot after the competition, whether I win or not. Either way I'll definitely be doing this again next year.
