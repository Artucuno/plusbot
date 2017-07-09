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
import importlib
import traceback
import logging
import asyncio
import threading
import datetime
import glob
import os
import aiohttp
from app.chat_formatting import pagify, box

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
    channell = bot.get_channel("332452782860926979")
    await bot.send_message(channell, msg)
    print("I have joinned the server {0}".format(serverName))
@bot.event
async def on_member_join(member):
    channel = bot.get_channel("332703848953151489")
    pm = "Hello {0} Welcome to {1} :smile: \n\nUse theese commands `+server` & `+invite` :smile:".format(member, member.server)
    msg = "{0} joinned {1} :smile:".format(member.mention, member.server)
    em = discord.Embed(color=0x42fc07)
    em.add_field(name='Join Log', value=("{0} joinned {1} :smile:".format(member.mention, member.server)))
    await bot.send_message(channel, embed=em)
    try:
        await bot.send_message(member, pm)
        print("Sent a message to {0}".format(member))
    except discord.HTTPException:
        print("Could Not send a message to {0}".format(member))
        pass
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel("332703848953151489")
    msg = "The user {0} left {1} :cry:".format(member.mention, member.server)
    umsg = "Bye Bye... :cry: Come back to {0} soon".format(member.server)
    try:
        await bot.send_message(member, umsg)
        print("Sent a message to {0}".format(member))
    except discord.HTTPException:
        print("Could Not send a message to {0}".format(member))
        pass
    em = discord.Embed(color=0xfc0606)
    em.add_field(name='Leave Log', value=("The user {0} left {1} :cry:".format(member.mention, member.server)))
    await bot.send_message(channel, embed=em)
@bot.event
async def on_server_remove(server):
    channel = bot.get_channel("332703848953151489")
    serverName = server.name
    serverOwner = server.owner
    serverMembers = server.member_count
    msg = "\n\nI have left a server :cry:\n**Server** : {}\n**Owner** : {}\n**Member Count** : {}".format(serverName, serverOwner, serverMembers)
    await bot.send_message(channel, msg)
    channell = bot.get_channel("332452782860926979")
    await bot.send_message(channell, msg)
@checks.is_owner()
@bot.command()
async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        """Kicks user."""
        author = ctx.message.author
        server = author.server

        if author == user:
            await bot.say("I cannot let you do that. Self-harm is "
                          "bad \N{PENSIVE FACE}")
            return
        elif not is_allowed_by_hierarchy(server, author, user):
            await bot.say("I cannot let you do that. You are "
                          "not higher than the user in the role "
                          "hierarchy.")
            return

        try:
            await bot.kick(user)
            logger.info("{}({}) kicked {}({})".format(
                author.name, author.id, user.name, user.id))
            await new_case(server,
                           action="KICK",
                           mod=author,
                           user=user,
                           reason=reason)
            await bot.say("Done. That felt good.")
        except discord.errors.Forbidden:
            await bot.say("I'm not allowed to do that.")
        except Exception as e:
            print(e)
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
    await bot.whisper(embed=em)
    chan = bot.get_channel("333171754698670080")
    msg = "{} used the command `+request`".format(user)
    await bot.send_message(chan, msg)
@bot.command(pass_context=True)
async def cmds(ctx):
    """Cmds"""
    author = ctx.message.author
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Cmds', value=("\n\n"
                                     "**==============================**\n"
                                     "+cmdsfun    fun comamnds\n"
                                     "+cmdsmusic  Music Commands\n"
                                     "+cmdsowner  Owner Commands\n"
                                     "+cmdsdb     + DiscordBot Commands\n"
                                     "\n"
                                     "**==============================**\n"
                                     "+server     See my server\n"
                                     "+invite     Invite me!\n"
                                     "**==============================**\n"
                                     "**My Partners!**:\n"
                                     "Please click on their names to invite them!\n"
                                     "[StormBot](https://discordapp.com/oauth2/authorize?client_id=301216578991816704&scope=bot&permissions=-1)\n"
                                     "[TerraBite](https://discordapp.com/oauth2/authorize?client_id=295942672890331147&scope=bot&permissions=2146958463)\n"
                                     "[BulletBot](https://discordapp.com/oauth2/authorize?client_id=333202518160965633&scope=bot&permissions=-1)"))
    em.set_footer(text="You can use +help but +cmds is better!")
    await bot.say(embed=em)
    channel = bot.get_channel("333171754698670080")
    msg = "{} used the command `+cmds`".format(author.mention)
    await bot.send_message(channel, msg)
@bot.command(pass_context=True)
async def cmdsfun(ctx):
    """Cmds"""
    author = ctx.message.author
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Cmds', value=("\n\n"
                                     "**==============================**\n"
                                     "+info   Info about me\n"
                                     "+embed  embed something!\n"
                                     "+say    make me say something!\n"))
    await bot.say(embed=em)
    channel = bot.get_channel("333171754698670080")
    msg = "{} used the command `+cmdsfun`".format(author.mention)
    await bot.send_message(channel, msg)
@bot.command(pass_context=True)
async def cmdsmusic(ctx):
    """Cmds"""
    author = ctx.message.author
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Cmds', value=("\n\n"
                                     "**==============================**\n"
                                     "+play  Play a song\n"
                                     "+stop  Stop dat\n"
                                     "+np    I am playing...\n"
                                     "+queue Whats next?"))
    await bot.say(embed=em)
    channel = bot.get_channel("333171754698670080")
    msg = "{} used the command `+cmdsmusic`".format(author.mention)
    await bot.send_message(channel, msg)
@bot.command(pass_context=True)
async def cmdsdb(ctx):
    """Cmds"""
    author = ctx.message.author
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Cmds', value=("\n\n"
                                     "**==============================**\n"
                                     "request  Request a bot\n"
                                     "accept   Accept a bot (Owner)\n"))
    await bot.say(embed=em)
    channel = bot.get_channel("333171754698670080")
    msg = "{} used the command `+cmdsdb`".format(author.mention)
    await bot.send_message(channel, msg)
@checks.is_owner()
@bot.command(pass_context=True)
async def servers(ctx):
    """Lists and allows to leave servers"""
    owner = ctx.message.author
    servers = sorted(list(bot.servers),
                     key=lambda s: s.name.lower())
    msg = ""
    for i, server in enumerate(servers):
        msg += "{}: {}\n".format(i, server.name)

    for page in pagify(msg, ['\n']):
        await bot.say(page)

    while msg is not None:
        msg = await bot.wait_for_message(author=owner, timeout=15)
        try:
            msg = int(msg.content)
            await leave_confirmation(servers[msg], owner, ctx)
            break
        except (IndexError, ValueError, AttributeError):
            pass
@bot.command(pass_context=True)
async def server(ctx):
    """My Server"""
    msg = "Here you go :smile: https://discord.gg/hQnp6nA"
    await bot.whisper(msg)
    await bot.say("Check your DM's :smile:")
@bot.command(pass_context=True)
async def cmdsowner(ctx):
    """Cmds"""
    author = ctx.message.author
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Cmds', value=("\n\n"
                                     "**==============================**\n"
                                     "+sga\n"
                                     "+sga2\n"
                                     "+sga3\n"
                                     "+sga4\n"
                                     "+sga5\n"
                                     "+sga6\n"
                                     "+sga7\n"
                                     "setgame  What am i doing?\n"
                                     "shutdown Shutting down...\n"))
    await bot.say(embed=em)
    channel = bot.get_channel("333171754698670080")
    msg = "{} used the command `+cmdsowner`".format(author.mention)
    await bot.send_message(channel, msg)
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
       mess = "@everyone "
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
       await bot.say("Sorry your server could not be bumped!\n"
                     "Try:\n"
                     "1) Give your default channel a description\n"
                     "\n"
                     "2) Join the Plus Server to get help\n"
                     "\n"
                     "3) Kick the bot then invite it again\n"
                     "\n"
                     "4) Use `+contact` to get help\n"
                     "and then")
    inv = await bot.create_invite(ctx.message.server)
    message = "Server: {0} \n Description: {1} \n Users: {2} \n  Invite: {3}".format(server, des, members, inv)
    try:
       bot.send_message(channel, embed=em)
       await bot.say("Your server was bumped :thumbsup: ")
       print("The server {} was bumped!".format(server.name))
    except discord.HTTPException:
       await bot.say("Sorry your server could not be bumped!\n"
                     "Try:\n"
                     "1) Give your default channel a description\n"
                     "\n"
                     "2) Join the Plus Server to get help\n"
                     "\n"
                     "3) Kick the bot then invite it again\n"
                     "\n"
                     "4) Use `+contact` to get help\n"
                     "and then")
@checks.is_owner()
@bot.command(pass_context=True)
async def pbump(ctx):
    """Bump your server!"""

    #Your code will go here
    server = ctx.message.server
    author = ctx.message.author
    des = server.default_channel.topic
    members = server.member_count
    count = 1
    try:
       mess = "@everyone "
       channel = bot.get_channel("333182027958321155")
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
       await bot.say("Sorry your server could not be bumped!\n"
                     "Try:\n"
                     "1) Give your default channel a description\n"
                     "\n"
                     "2) Join the Plus Server to get help\n"
                     "\n"
                     "3) Kick the bot then invite it again\n"
                     "\n"
                     "4) Use `+contact` to get help\n"
                     "and then")
    inv = await bot.create_invite(ctx.message.server)
    message = "Server: {0} \n Description: {1} \n Users: {2} \n  Invite: {3}".format(server, des, members, inv)
    try:
       bot.send_message(channel, embed=em)
       await bot.say("Your server was bumped :thumbsup: ")
       print("The server {} was bumped!".format(server.name))
    except discord.HTTPException:
       await bot.say("Sorry your server could not be bumped!\n"
                     "Try:\n"
                     "1) Give your default channel a description\n"
                     "\n"
                     "2) Join the Plus Server to get help\n"
                     "\n"
                     "3) Kick the bot then invite it again\n"
                     "\n"
                     "4) Use `+contact` to get help\n"
                     "and then")
@bot.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    em = discord.Embed(color=author.colour)
    em.add_field(name='Invite :smile:', value=("[Invite Here!](https://discordapp.com/oauth2/authorize?client_id=327949245980213250&scope=bot&permissions=-1)"))
    await bot.say(embed=em)
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
    em.add_field(name='Memory usage:', value=mem_usage + " / 15.5 GB")
    em.add_field(name='Ping', value=(str(round((t2-t1)*1000)) + "ms"))
    em.add_field(name='Server Count', value=(len(bot.servers)))
    em.add_field(name='User Count', value=(len(set(bot.get_all_members()))))
    em.add_field(name='Version', value=(dpy_version))
    em.add_field(name='Description', value=("[Plus](https://python.org) is a W.I.P Discord Bot"))
    em.set_footer(text='Owner : {} {}'.format(config.OWNER, config.OID))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/332063444327071754/332088067269853185/P.png")
    await bot.say(embed = em)
@bot.command()
async def contact(user, serverinvite, msg=""):
    """Help me!"""
    try:
        channel = bot.get_channel("332452782860926979")
        em = discord.Embed(color=0x0BFCF2)
        em.add_field(name='Contact', value=("\nUser : {}\nServer Invite : {}\nMessage : {}".format(user, serverinvite, msg)))
        await bot.send_message(channel, embed=em)
        em = discord.Embed(color=0x0BFCF2)
        em.add_field(name='Contact', value=("Your message was sent\nMessage : [{}](.)".format(msg)))
        await bot.say(embed=em)
    except discord.HTTPException:
        await bot.say("Your Message could not be sent!\n"
                      "1) The Route ID may be unavalable\n"
                      "\n"
                      "2) My ping may be too slow\n"
                      "\n"
                      "3) A command may be stopping `+contact`")
@bot.command(pass_context=True)
async def roll(ctx):
    """1. 2. 3. 4. 5. 6."""
    author = ctx.message.author
    r = ["1", "2", "3", "4", "5", "6"]
    em = discord.Embed(color=author.colour)
    em.add_field(name='Roll Result', value=("```\n{}\n```".format(random.choice(r))))
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
@bot.command()
async def say(msg):
    """Hi"""
    await bot.say(msg)

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
@checks.is_owner()
@bot.command(pass_context=True)
async def sga6(ctx):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name='+cmds | {} Guilds | {} Users'.format(len(bot.servers), len(set(bot.get_all_members())))))
@checks.is_owner()
@bot.command(pass_context=True)
async def sga7(ctx):
    """Owner Command!"""
    await bot.change_presence(game=discord.Game(name='+cmds | {} Users'.format(len(set(bot.get_all_members())))))
@bot.command()
async def order(user, food):
    """Order food"""
    await bot.say("Your food has been ordered! ({})".format(user))
    channel = bot.get_channel("333474387799834634")
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Order', value=("There was an order sent! ({}) by {}".format(food, user)))
    await bot.send_message(channel, embed=em)
@bot.command(pass_context=True)
async def joindb(ctx):
    """Join + Discord Bots"""
    await bot.say("\n"
                  "**Description**:\n"
                  "+ Discord Bots is where you can add your bot\n"
                  "and test other bots!\n"
                  "\nInvite : https://discord.gg/Fca6FGs\n")
@bot.command(pass_context=True)
async def joindc(ctx):
    """Join Discord Cafe"""
    await bot.say("\n"
                  "**Description**:\n"
                  "The Discord Cafe is a place where everyone can\n"
                  "Chat and have fun!\n"
                  "\nInvite : https://discord.gg/Q7NkYhu\n")
@bot.command(pass_context=True)
async def partner(ctx):
    """Partner with me!"""
    await bot.whisper("Hello so i heard you want to partner?\n"
                      "if you do talk to <@321193377951645699>\n"
                      "and we will arange a meeting\n"
                      "We will partner:\n"
                      "Bots\n"
                      "Servers\n"
                      "or just share code to help you with your projects")
    await bot.say("Check your DM's")
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Serverinfo"""
    import datetime
    server = ctx.message.server
    author = ctx.message.author
    text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    total = text_channels + voice_channels
    serverName = server.name
    serverOwner = server.owner
    serverMembers = server.member_count
    passed = (ctx.message.timestamp - server.created_at).days
    created_at = ("Since {}. That's over {} days ago!"
                  "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                            passed))
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Created at', value=(created_at))
    em.add_field(name='Server', value=(server))
    em.add_field(name='Server Owner', value=(serverOwner))
    em.add_field(name='Member Count', value=(serverMembers))
    em.add_field(name='Region', value=(server.region))
    em.add_field(name='Text Channels', value=(text_channels))
    em.add_field(name='Voice Channels', value=(voice_channels))
    em.add_field(name='Total Channels', value=(total))
    em.set_thumbnail(url=server.icon_url)
    await bot.say(embed=em)

# Boot / Start bot
print("Plus + Discord Bot :)")
wait()
bot.run(config.TOKEN)
