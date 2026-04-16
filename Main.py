#Setting up Discord Library and Bot
import asyncio
import db
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

# Other imports
import os
import time
from datetime import datetime, timedelta, UTC
import random
from cardPacks import openRegularPack, openIGLPack, openAWPPack

#sETTING UP THE BOT
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

load_dotenv()
token = os.getenv("DISCORD_TOKEN") 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

#Command Help
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Command Help", description="List of available commands:", color=0x060f12)
    embed.add_field(name="!joke", value="Fetches a random dark joke.", inline=False)
    embed.add_field(name="!clear <amount>", value="Clears a specified number of messages. (Requires Manage Messages permission)", inline=False)
    await ctx.send(embed=embed)



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



#clearing messages command, only for users with manage_messages permission
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    # Check if the user has the required permissions
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send('You do not have permission to use this command.', delete_after=5)
        return
    
    name = ctx.author.mention  # Get the user's mention for output
    # Validate the amount of messages to clear
    if amount < 1:
        await ctx.send('Please specify a positive number of messages to clear.', delete_after=5)
        return
    
    if amount > 100:
        await ctx.send('You can only clear up to 100 messages at a time.', delete_after=5)
        return
    
    #output the name of the user who issued the command and the amount of messages cleared
    await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message itself
    await ctx.send(f'Successfully cleared {amount} messages by {name}✅', delete_after=5)



#balance command to show the user's balance in an embed
@bot.command()
async def balance(ctx):
    user_id = ctx.author.id
    user_data = db.get_user(user_id)
    balance = user_data["balance"]
    embed = discord.Embed(title=f"{ctx.author.name}'s Balance", description=f"You have {balance} coins 💰", color=0x060f12)
    await ctx.send(embed=embed)

#profile command to show the user's balance, level, and cards in an embed
@bot.command()
async def profile(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author
    user_id = user.id
    user_data = db.get_user(user_id)
    balance = user_data["balance"]
    level = user_data["level"]
    cards = len(user_data["cards"]) if user_data["cards"] else 0

    #Buttons
    inventrory_button = Button(label="Inventory", style=discord.ButtonStyle.blurple)


    embed = discord.Embed(title=f"{user.name}'s Profile", color=0x060f12)
    embed.add_field(name="Balance", value=f"{balance} coins 💰", inline=False)
    embed.add_field(name="Level", value=f"Level {level} 🏆", inline=False)
    embed.add_field(name="Cards", value=f"{cards} 🃏", inline=False)

    await ctx.send(embed=embed)    


#Plays sound in the user's voice channel, if they are in one, and disconnects after the sound is done playing
@bot.command()
async def sound(ctx):
    print(f"User {ctx.author} issued the sound command")
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send("Ты не в войсе")
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


@bot.command()
async def openpack(ctx):

    async def button_callback(interaction: discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("That's not your pack!", ephemeral=True)
            return

        player = openRegularPack()
        db.add_card(ctx.author.id, player)

        if player["Rarity"] == "Common":
            embed_color = 0x00d443
        elif player["Rarity"] == "Rare":
            embed_color = 0x8600d4
        elif player["Rarity"] == "Elite":
            embed_color = 0xd40000
        else:
            embed_color = 0xf1c40f

        embed = discord.Embed(
            title="You opened a pack!",
            description=f"You got {player['Name']} ({player['Rarity']})",
            color=embed_color
        )

        await interaction.response.send_message(embed=embed)  # 👈 ВАЖНО

    OpenPack_Button = Button(label="Open Pack", style=discord.ButtonStyle.green)
    OpenPack_Button.callback = button_callback

    view = View()
    view.add_item(OpenPack_Button)

    await ctx.send(
        "Pack: 50% Regular, 30% IGL, 20% AWP",
        view=view
    )

#clearing any errors that may occur with the clear command
@bot.event
# Handle command errors globally
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            'This command does not exist. Use !help to see the list of available commands',
            delete_after=5
        )

@bot.event
async def on_error(event, *args, **kwargs):
    import traceback
    print(traceback.format_exc())
# Handle errors specific to the clear command
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        ctx.delete_after = 5
        await ctx.send('Please specify the number of messages to clear. Usage: !clear <amount>', delete_after=5)
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Please provide a valid number for the amount of messages to clear', delete_after=5)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command', delete_after=5)
    else:
        await ctx.send('An error occurred while trying to clear messages', delete_after=5)

#Owners command to send an announcement to all users who have used the bot, by sending them a DM with the announcement message
@bot.command()
@commands.is_owner()  # only YOU can run this
async def announce(ctx, *, message):
    for user_id in db["users"]:
        try:
            user = await bot.fetch_user(int(user_id))
            await user.send(f"📢 Update:\n{message}")
        except:
            continue  # user has DMs closed or error

@bot.command()
@commands.is_owner()
async def clearData(ctx):
    db.save_data({"users": {}})
    await ctx.send("All user data has been cleared.")

@bot.command()
@commands.is_owner()
async def addMoney(ctx, user: discord.User, amount: int):
    db.add_money(user.id, amount)
    await ctx.send(f"Added {amount} coins to {user.mention}'s balance.")

bot.run(token)