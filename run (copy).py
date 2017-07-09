from app import checks
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import logging
import sys
import os
from app import config
import asyncio
import random

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
description = '''TIP : you can use +cmds its better!'''
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive
def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")

# Commands
@bot.event
async def on_server_join(server):
    channel = bot.get_channel("332703848953151489")
    serverName = server.name
    serverOwner = server.owner
    serverMembers = server.member_count
    msg = "\n\nYAY IVE JOINNED A NEW SERVER! :white_check_mark: :smile:\n**Server** : {0}\n**Owner** : {1}\n**Member Count** : {2}\nI am now on **{3}** Servers!\n\n".format(serverName, serverOwner, serverMembers, len(bot.servers))
    await bot.send_message(channel, msg)
    msgt = "i have joinned a new server! :smile:"
    channelt = bot.get_channel("327958586959462410")
    await bot.send_message(channelt, msgt)
    print("I have joinned the server {0}".format(serverName))
@bot.event
async def on_member_join(member):
    channel = bot.get_channel("332703848953151489")
    pm = "Hello {0} Welcome to {1} :smile: \n\nUse theese commands `+server` & `+invite` :smile:".format(member, member.server)
    msg = "{0} joinned {1} :smile:".format(member.mention, member.server)
    await bot.send_message(channel, msg)
    try:
        await bot.send_message(member, pm)
        print("Sent a message to {0}".format(member))
    except discord.HTTPException:
        print("Could Not send a message to {0}".format(member))
        pass
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel("332703848953151489")
    msg = "the user {0} left {1}".format(member.mention, member.server)
    umsg = "Bye Bye... :cry: Come back to {0} soon".format(member.server)
    try:
        await bot.send_message(member, umsg)
        print("Sent a message to {0}".format(member))
    except discord.HTTPException:
        print("Could Not send a message to {0}".format(member))
        pass
    await bot.send_message(channel, msg)
@bot.event
async def on_server_remove(server):
    channel = bot.get_channel("332703848953151489")
    serverName = server.name
    serverOwner = server.owner
    serverMembers = server.member_count
    msg = "\n\nI have left a server :cry:\n**Server** : {}\n**Owner** : {}\n**Member Count** : {}".format(serverName, serverOwner, serverMembers)
    await bot.send_message(channel, msg)
@bot.command()
async def accept(user, botname):
    """Request a bot"""
    channel = bot.get_channel("332835741719592972")
    msg = "{} your bot {} was accepted!".format(user, botname)
    await bot.send_message(channel, msg)
@bot.command()
async def request(url, user):
    """Request a bot"""
    mention = "<@321193377951645699> "
    channel = bot.get_channel("332835741719592972")
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Request', value=("User : {}\n\nUrl : {}".format(user, url)))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/327958586959462410/332838425449332739/plus3.png")
    await bot.send_message(channel, mention)
    await bot.send_message(channel, embed=em)
    await bot.say("Check your DM's")
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Request', value=("Your Request was sent!\n\nUrl : {}\nYour Bot was sent [here](https://discord.gg/Fca6FGs)!".format(url)))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/327958586959462410/332838425449332739/plus3.png")
    await bot.whisper(embed=em)
@bot.command(pass_context=True)
async def server(ctx):
    """My Server"""
    msg = "Here you go :smile: https://discord.gg/hQnp6nA"
    await bot.whisper(msg)
@bot.command(pass_context=True)
async def website(ctx):
    """my website"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Website', value=("Here is my [website!](https://articuno1234.github.io/plus/)"))
    await bot.say(embed=em)
@bot.command(pass_context=True)
async def cmds(ctx):
    """Help"""
    import time
    author = ctx.message.author
    msg = await bot.say("{} Check your DM's".format(author.mention))
    time.sleep(2)
    em = discord.Embed(color=author.colour)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/332063444327071754/333041127693221890/plus3.png")
    await bot.say(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Servers :computer: ', value=("I am currently in **{}** servers".format(len(bot.servers))))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Music :musical_note: ', value=("\n**play**  Play a song\n\n**pause**  ||\n\n**np**  Now Playing\n\nCredits to `Just-Some-Bots`"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Fun :8ball: ', value=("\n**roll**  Roll a dice\n\n**imput** Imput something\n\n**cleverbot**  Talk to me!\n\n**dog**  WOOF!"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Info :information_source: ', value=("\n**invite**  invite me!\n\n**info**  Info about me\n\n**ping**  pong.\n\n**contact** HELP ME (put you name in message)\n"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='+ Discord Bots', value=("\n**request**  Request a bot\n\n**remove** Comming soon!\n\n**join**  Join + Discord Bots"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Owner Commands :tools: ', value=("\n**sga**\n\n**sga2**\n\n**sga3**\n\n**sga4**\n\n**sga5**\n\n**shutdown**\n\n**setgame**"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=author.colour)
    em.set_footer(text="```Type +help command for more info on a command.\n"
                       "You can also type +help category for more info on a category.```")
    await bot.whisper(embed=em)
@bot.command(pass_context=True)
async def join():
    """Join + Discord Bots"""
    await bot.say("Check Your DM's")
    await bot.whisper("Here you go! :smile: https://discord.gg/Fca6FGs")
@bot.command()
async def contact(msg):
    """HELP ME!"""
    channel = bot.get_channel("332452782860926979")
    contac = "**Contact**"
    await bot.send_message(channel, contac)
    await bot.send_message(channel, msg)
    await bot.say("Your message was sent! :mailbox_with_mail: ")
@bot.command(pass_context=True)
async def dog(ctx):
    """WOOF!"""
    images = ["https://www.cesarsway.com/sites/newcesarsway/files/styles/large_article_preview/public/Common-dog-behaviors-explained.jpg?itok=FSzwbBoi", "https://static.pexels.com/photos/7720/night-animal-dog-pet.jpg", "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg", "https://www.what-dog.net/Images/faces2/scroll0015.jpg", "http://users.atw.hu/kedvenckutyank/images/kutya2.jpg", "https://www.cesarsway.com/sites/newcesarsway/files/styles/large_article_preview/public/Why%20dogs%20eat%20grass_0.jpg?itok=fu5yHnol", "https://s-media-cache-ak0.pinimg.com/736x/63/0f/0e/630f0ef3f6f3126ca11f19f4a9b85243--dachshund-puppies-weenie-dogs.jpg"]
    await bot.say(random.choice(images))
@bot.command(pass_context=True)
async def cleverbot(ctx):
    """Talk to Me"""
    words = ["Ok", "How are you", "cool :smile:", "Good", "oh.", "really?", "What do you like?", "Do you like XBox?", "Will you marry me?", "hello :smile:","oh really?", "Do you like music?", "No.", "Yes", "I like cheese", "Behind You!", "hmmm...", "1. 2. 3. 4. 5."]
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Awnser :speech_balloon:', value=(random.choice(words)))
    await bot.say(embed=em)
@bot.command()
async def embed(msg):
    """embed message"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Embed', value=(msg))
    await bot.say(embed=em)
@bot.command(pass_context=True)
async def prefix(ctx):
    await bot.say(config.PREFIX)
@bot.command(pass_context=True)
async def roll(ctx):
    """1. 2. 3. 4. 5. 6."""
    author = ctx.message.author
    r = ["1", "2", "3", "4", "5", "6"]
    em = discord.Embed(color=author.colour)
    em.add_field(name='Roll Result', value=("```\n{}\n```".format(random.choice(r))))
    await bot.say(embed=em)
@bot.command(pass_context=True)
async def ping(ctx):
    """Pong."""
    import time
    ping = await bot.say("Pong. :ping_pong: ")
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    await bot.delete_message(ping)
    aping = await bot.say("Pong. :ping_pong:  `{}`".format(str(round((t2-t1)*1000))))
    await bot.edit_message(ping, aping)
@checks.is_owner()
@bot.command(pass_context=True)
async def shutdown(ctx):
    """Owner Command!"""
    await bot.say("Shutting Down... :wave: ")
    sys.exit(1)
@checks.is_owner()
@bot.command()
async def setgame(game):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name=game))
    await bot.say("Plus's game was set to {}".format(game))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga(ctx):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name='+cmds | {} Servers | {} Users'.format(len(bot.servers), len(set(bot.get_all_members())))))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga2(ctx):
    """Owner Command!"""
    import time
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    await bot.change_presence(game=discord.Game(name='+cmds | Ping {}'.format(str(round((t2-t1)*1000)) + "ms")))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga3(ctx):
    """Owner Command!"""
    mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    await bot.change_presence(game=discord.Game(name='+cmds | {}'.format(mem_usage)))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga4(ctx):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name='+cmds | Running off a USB!'))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga5(ctx):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name='+cmds | v{}'.format(discord.__version__)))
@bot.command(pass_context=True)
async def info(ctx):
    """info about me!"""
    import time
    dpy_repo = "https://github.com/Rapptz/discord.py"
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    dpy_version = "[{}]({})".format(discord.__version__, dpy_repo)
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Bot Owner', value=(config.OWNER))
    mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    em.add_field(name='Memory usage:', value=mem_usage)
    em.add_field(name='Ping', value=(str(round((t2-t1)*1000)) + "ms"))
    em.add_field(name='Server Count', value=(len(bot.servers)))
    em.add_field(name='User Count', value=(len(set(bot.get_all_members()))))
    em.add_field(name='Version', value=(dpy_version))
    em.add_field(name='Description', value=("[Plus](https://python.org) is a W.I.P Discord Bot"))
    em.set_footer(text='Owner : {} {}'.format(config.OWNER, config.OID))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/332063444327071754/332088067269853185/P.png")
    await bot.say(embed = em)

@bot.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    em = discord.Embed(color=author.colour)
    em.add_field(name='Invite :smile:', value=("[Invite Here!](https://discordapp.com/oauth2/authorize?client_id=327949245980213250&scope=bot&permissions=-1)"))
    await bot.say(embed=em)
    em = discord.Embed(color=author.colour)
    em.add_field(name='Thanks', value=("Thankyou for using **Plus +**"))
    await bot.say(embed=em)
@bot.command(pass_context=True)
async def bump(ctx):
    """Bump your server!"""

    #Your code will go here
    server = ctx.message.server
    author = ctx.message.author
    des = server.default_channel.topic
    members = server.member_count
    count = 1
    try:
       channel = bot.get_channel("332105685758115840")
       em = discord.Embed(color=0xea7938) #0xea7938 is the color code
       em.add_field(name='Name', value=server.name)
       em.add_field(name='Owner', value=server.owner)
       em.add_field(name='Description', value=server.default_channel.topic)
       em.add_field(name='invite', value=await bot.create_invite(ctx.message.server))
       em.add_field(name='Member Count', value=server.member_count)
       em.set_footer(text="Server Bumped by {0}".format(author))
       em.set_thumbnail(url=server.icon_url) #Or insert actual URL
       await bot.send_message(channel, embed=em)
       server = ctx.message.server
       des = server.default_channel.topic
       members = server.member_count
    except discord.HTTPException:
       await bot.say("Sorry your server could not be bumped!")
       pass
    try:
       inv = await bot.create_invite(ctx.message.server)
    except discord.HTTPException:
       await bot.say("Sorry your server could not be bumped!")
       pass
    message = "Server: {0} \n Description: {1} \n Users: {2} \n  Invite: {3}".format(server, des, members, inv)
    try:
       bot.send_message(channel, embed=em)
    except discord.HTTPException:
       await bot.say("Sorry your server could not be bumped!")
    await bot.say("Your server was bumped :thumbsup: ")
    print("The server {} was bumped!".format(server.name))
@bot.command()
async def imput(imput):
    """Imput something +imput (imput)"""
    await bot.say("```" + "py\n"
                  "Result:\n"
                  "'{}'\n"
                  "```".format(imput))

# Boot / Start bot
print("Plus + Discord Bot :)")
wait()
bot.run(config.TOKEN)
