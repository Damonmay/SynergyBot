# Created 20220714
# Discord bot
# First Priority to recognize the word Synergy


import discord
# import synergyWords.txt
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print("I'm ALIVE")

# @client.command()
# async def hello(ctx):
# 	await ctx.send("Hello, I'm the Synergy bot")


@client.event
async def on_message(message):

    messageContent = message.content.lower()

    if 'synergy' in messageContent:
    	await message.channel.send("SYNERGY") #maybe add some variable statements here


client.run('TokenBot')
#whoops, accidentedly uploaded token



