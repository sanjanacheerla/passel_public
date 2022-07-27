from random import randrange

import discord
from discord.ext import commands

# Author: hyppytyynytyydytys#1010
# Created: 26 MAY 2020
# Last updated: 17 JULY 2022
# About: This is a version of Passel Bot that should ONLY be used as a private server bot.
#        Follow the instructions here on how to set up with heroku:
#
#        Passel Bot is a solution to the number of limited number of pins in a discord server.
#        It manages pins in 2 modes, Mode 1 and Mode 2. 
#
#        More information can be found on https://passelbot.wixsite.com/home
#        Passel Support Server: https://discord.gg/wmSsKCX
#
#        Mode 1: In mode 1, the most recent pinned message gets sent to a pins archive
#        channel of your choice. This means that the most recent pin wont be viewable in
#        the pins tab, but will be visible in the pins archive channel that you chose during setup
#
#        Mode 2: In mode 2, the oldest pinned message gets sent to a pins archive channel of
#        your choice. This means that the most recent pin will be viewable in the pins tab, and
#        the oldest pin will be unpinned and put into the pins archive channel
#
#        Furthermore: the p.sendall feature described later in the code allows the user to set
#        Passel so that all pinned messages get sent to the pins archive channel.

# TODO change command here if you want to use another command, replace p. with anything you want inside the single ('') quotes
client = commands.Bot(command_prefix='p.',
                      status='Online', case_insensitive=True)
client.remove_command("help")

# TODO change mode to 1 or 2 here
mode = 1

# TODO 
# sendall is set to 0 by default, change to 1 if you want
# the bot to send all pinned messages to the pins channel
sendall = 0

# TODO 
# replace the 0 with the pins channel ID for your sever
pins_channel = 0

# TODO
# add any black listed channel IDs as a list separated by a comma (,)
# a good idea is to add admin channels to this
blacklisted_channels = []

# discord embed colors
EMBED_COLORS = [
    discord.Colour.magenta(),
    discord.Colour.blurple(),
    discord.Colour.dark_teal(),
    discord.Colour.blue(),
    discord.Colour.dark_blue(),
    discord.Colour.dark_gold(),
    discord.Colour.dark_green(),
    discord.Colour.dark_grey(),
    discord.Colour.dark_magenta(),
    discord.Colour.dark_orange(),
    discord.Colour.dark_purple(),
    discord.Colour.dark_red(),
    discord.Colour.darker_grey(),
    discord.Colour.gold(),
    discord.Colour.green(),
    discord.Colour.greyple(),
    discord.Colour.orange(),
    discord.Colour.purple(),
    discord.Colour.magenta(),
]

# When the bot is ready following sets the status of the bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Command to check what the settings of the bot
@client.command(name='settings', pass_context=True)
async def settings(ctx):
    if not ctx.message.author.guild_permissions.administrator:
        return

    await ctx.send("The mode you have setup is: " + str(mode))
    await ctx.send("Sendall is toggled to: " + str(sendall))
    await ctx.send("The pins channel for this server is: " + ctx.channel.guild.get_channel(pins_channel).mention)
    await ctx.send("Black listed channels are: ")
    for c in blacklisted_channels:
        try:
            await ctx.send(ctx.channel.guild.get_channel(c).mention)
        except:
            await ctx.send("Error: Check black listed channels")
            return
    await ctx.send("done")


@client.command(name='pins', pass_context=True)
async def pins(ctx):
    numPins = await ctx.message.channel.pins()
    await ctx.send(ctx.message.channel.mention + " has " + str(len(numPins)) + " pins.")

# The method that takes care of pin updates in a server
@client.event
async def on_guild_channel_pins_update(channel, last_pin):
    global data
    try:
        randomColor = randrange(len(EMBED_COLORS))
        numPins = await channel.pins()

        # checks to see if message is in the blacklist
        # message is only sent if there is a blacklisted server with 50 messages pinned, informs them
        # that passel is in the server and they can un-blacklist the channel to have passel work
        if str(channel.id) in blacklisted_channels:
            return

        isChannelThere = False
        # checks to see if pins channel exists in the server
        channnelList = channel.guild.channels
        for channel in channnelList:
            if int(pins_channel) == int(channel.id):
                isChannelThere = True

        # checks to see if pins channel exists or has been deleted
        if not isChannelThere:
            await channel.send("Check to see if the pins archive channel during setup has been deleted")
            return

        # only happens if send all is toggled on
        if len(numPins) < 49 and sendall == 1:
            last_pinned = numPins[0]
            pinEmbed = discord.Embed(
                description="\"" + last_pinned.content + "\"",
                colour=EMBED_COLORS[randomColor]
            )
            # checks to see if pinned message has attachments
            attachments = last_pinned.attachments
            if len(attachments) >= 1:
                pinEmbed.set_image(url=attachments[0].url)
            pinEmbed.add_field(
                name="Jump", value=last_pinned.jump_url, inline=False)
            pinEmbed.set_footer(
                text="sent in: " + last_pinned.channel.name + " - at: " + str(last_pinned.created_at))
            pinEmbed.set_author(name='Sent by ' + last_pinned.author.name)
            await channel.guild.get_channel(int(pins_channel)).send(embed=pinEmbed)
            
            # remove this message if you do not want the bot to send a message when you pin a message
            await last_pinned.channel.send(
                "See pinned message in " + channel.guild.get_channel(int(pins_channel)).mention)
            return

        # if guild mode is one does the process following mode 1
        if mode == 1:
            last_pinned = numPins[len(numPins) - 1]
            # sends extra messages
            if len(numPins) == 50:
                last_pinned = numPins[0]
                pinEmbed = discord.Embed(
                    # title="Sent by " + last_pinned.author.name,
                    description="\"" + last_pinned.content + "\"",
                    colour=EMBED_COLORS[randomColor]
                )
                # checks to see if pinned message has attachments
                attachments = last_pinned.attachments
                if len(attachments) >= 1:
                    pinEmbed.set_image(url=attachments[0].url)
                pinEmbed.add_field(
                    name="Jump", value=last_pinned.jump_url, inline=False)
                pinEmbed.set_footer(
                    text="sent in: " + last_pinned.channel.name + " - at: " + str(last_pinned.created_at))
                pinEmbed.set_author(name='Sent by ' + last_pinned.author.name)
                await channel.guild.get_channel(int(pins_channel)).send(embed=pinEmbed)

                # remove this message if you do not want the bot to send a message when you pin a message
                await last_pinned.channel.send(
                    "See pinned message in " + channel.guild.get_channel(int(pins_channel)).mention)
                await last_pinned.unpin()

        # if guild mode is two follows the process for mode 2
        if mode == 2:
            last_pinned = numPins[0]
            if len(numPins) == 50:
                last_pinned = numPins[len(numPins) - 1]
                pinEmbed = discord.Embed(
                    # title="Sent by " + last_pinned.author.name,
                    description="\"" + last_pinned.content + "\"",
                    colour=EMBED_COLORS[randomColor]
                )
                # checks to see if pinned message has attachments
                attachments = last_pinned.attachments
                if len(attachments) >= 1:
                    pinEmbed.set_image(url=attachments[0].url)
                pinEmbed.add_field(
                    name="Jump", value=last_pinned.jump_url, inline=False)
                pinEmbed.set_footer(
                    text="sent in: " + last_pinned.channel.name + " - at: " + str(last_pinned.created_at))
                pinEmbed.set_author(name='Sent by ' + last_pinned.author.name)
                await last_pinned.guild.get_channel(int(pins_channel)).send(embed=pinEmbed)

                # remove this message if you do not want the bot to send a message when you pin a message
                await last_pinned.channel.send(
                    "See oldest pinned message in " + channel.guild.get_channel(int(pins_channel)).mention)
                await last_pinned.unpin()
    except:
        print("unpinned a message, not useful for bot so does nothing")


# TODO Replace TOKEN with the token from discord developer portal
client.run('TOKEN')
