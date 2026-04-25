import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio

def setup(bot, db):
    # Command to fetch and send a joke
    @bot.command()
    async def joke(ctx):
        import requests 
        url = "https://v2.jokeapi.dev/joke/dark?type=twopart"
        response = requests.get(url)
        data = response.json()
        firstPart = data["setup"]
        secondPart = data["delivery"]
        await ctx.send(firstPart)
        await asyncio.sleep(2)
        await ctx.send(secondPart)

    #Plays sound in the user's voice channel, if they are in one, and disconnects after the sound is done playing
    @bot.command()
    async def sound(ctx):
        if not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("User is not connected to a voice channel.", delete_after=5)
            return

        channel = ctx.author.voice.channel


        if ctx.voice_client:
            await ctx.voice_client.disconnect()

        voice_client = await channel.connect()

        audio_source = discord.FFmpegPCMAudio("secretSound.wav")

        voice_client.play(audio_source)

        while voice_client.is_playing():
            await asyncio.sleep(1)

        await voice_client.disconnect()