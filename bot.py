import discord
import os
import random
import discord.ext
from discord.ext import commands
import nacl
client = commands.Bot(discord.Intents.all())
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!leave"):
        print("Left voice")
        await message.guild.voice_client.disconnect()
    elif message.content.startswith("do you like vodka"):
        await message.channel.send("да где это")
    elif message.content.startswith("that was just a joke"):
        await discord.Member.kick(message.author)
    elif message.content.startswith("!play"):
        print("Playing song")
        audio_source = discord.FFmpegPCMAudio("anthem.mp3")
        voice = await message.author.voice.channel.connect()
        voice.play(audio_source)
client.run('token')
