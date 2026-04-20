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
    embedError = discord.Embed(title="Some Error have occured :/", color=0xFFFFFF)
    if not ctx.author.guild_permissions.manage_messages:
        embedError.add_field(name="You do not have permission to use this command.")
        await ctx.send(embed=embedError, delete_after=5)
        return
    
    name = ctx.author.mention  # Get the user's mention for output
    # Validate the amount of messages to clear
    if amount < 1:
        embedError.add_field(name="Please specify a positive number of messages to clear.")
        await ctx.send(embed=embedError, delete_after=5)
        return
    
    if amount > 500:
        embedError.add_field(name='You can only clear up to 500 messages at a time.')
        await ctx.send(embed=embedError, delete_after=5)
        return
    
    embedSuccesfull = discord.Embed(title=f"Cleaning Been Completed✅", color=0x00FF04)
    #output the name of the user who issued the command and the amount of messages cleared
    await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message itself
    await ctx.send(embed=embedSuccesfull, delete_after=5)



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

    nextpage_button = Button(label=">", style=discord.ButtonStyle.blurple)

    previouspage_button = Button(label="<", style=discord.ButtonStyle.blurple)


    embed = discord.Embed(title=f"Profile Information", color=0x060f12)
    embed.add_field(name="Balance", value=f"${balance}         Level {level} 🏆            {cards} 🃏", inline=False)


    await ctx.send(embed=embed)    


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

#open pack command to open a card pack and add the card to the user's collection, with a button to open the pack and an embed to show the card that was opened, with different colors for different rarities
#We need to work on the system to day, to make everything looks clean on work properly.
@bot.command()
async def open(ctx):
    #Pack price is 175 coins, check if the user has enough coins to open the pack
    user_id = ctx.author.id
    user = ctx.author
    user_data = db.get_user(user_id)
    balance = user_data["balance"]
    
    
    async def button_callback(interaction: discord.Interaction):
        if interaction.user != user:
            await interaction.response.send_message("That's not your pack!", ephemeral=True, delete_after=5)
            return
        if balance < 175:
            balance_needed = 175 - balance  
            embed = discord.Embed(title="Oh nooooo! :(",
                                   description=f"You need {balance_needed} more coins to open a pack.", 
                                   color=0xff0000)
            await interaction.message.delete(   )
            await ctx.send(embed=embed)
            return

        player = openRegularPack()
        db.subtract_money(ctx.author.id, 175)

        await interaction.message.delete(   )

        if player["Rarity"] == "Common":
            embed_color = 0x00d443
        elif player["Rarity"] == "Rare":
            embed_color = 0x8600d4
        elif player["Rarity"] == "Elite":
            embed_color = 0xd40000
        else:
            embed_color = 0xf1c40f


        keepOrSell = View()
        async def keep(interaction: discord.Interaction):
            if interaction.user != user:
                await interaction.followup.send("That's not your card!", ephemeral=True, delete_after=5)
                return
            db.add_card(ctx.author.id, player)
            
            await interaction.response.edit_message(
            content="✅ Card added to your collection!",
            view=None
            )

        async def sell(interaction: discord.Interaction):
            if interaction.user != user:
                await interaction.followup.send("That's not your card!", ephemeral=True, delete_after=5)
                return
            db.add_money(ctx.author.id, player['Price'])

            await interaction.response.edit_message(
            
            content=f"Card was sold for {player['Price']}",
            view=None
            )

        keepCard = Button(label="KEEP", style=discord.ButtonStyle.grey)
        keepCard.callback = keep

        sellCard = Button(label="SELL", style=discord.ButtonStyle.red)
        sellCard.callback = sell

        keepOrSell.add_item(keepCard)
        keepOrSell.add_item(sellCard)

        
        embed = discord.Embed(
            title=f"You got {player['Name']}!",
            description=f"Rarity: {player['Rarity']}\nRating: {player['Rating']}\nRole: {player['Role']}\nCountry: {player['Country']}\n\nPrice: {player['Price']}",
            color=embed_color,
        )

        await interaction.response.send_message(embed=embed, view = keepOrSell) 
    
    async def regularOpen(interaction: discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.message.delete(   )
            await interaction.response.send_message("That's not your pack!", ephemeral=True)
            return
        if balance < 175:
            balance_needed = 175 - balance  
            embed = discord.Embed(title="Oh nooooo! :(",
                                   description=f"You need {balance_needed} more coins to open a pack.", 
                                   color=0xff0000)
            await interaction.message.delete(   )
            await ctx.send(embed=embed)
            return
        

        player = openRegularPack()
        db.subtract_money(ctx.author.id, 175)
        
        await interaction.response.send_message("Opening pack...")

        slowOpen = await interaction.original_response()

        await asyncio.sleep(2)
        await slowOpen.edit(content=f"Opening pack...\n\n{player['Country']}")

        await asyncio.sleep(2)
        await slowOpen.edit(content=f"Opening pack...\n\n{player['Country']}\n{player['Role']}")

        await asyncio.sleep(2)
        await slowOpen.edit(content=f"Opening pack...\n\n{player['Country']}\n{player['Role']}\n{player['Team']}")

        await asyncio.sleep(2)
        await slowOpen.edit(content=f"Opening pack...\n\n{player['Country']}\n{player['Role']}\n{player['Team']}\n{player['Rarity']}")

        await asyncio.sleep(2)

        await interaction.message.delete(   )

        if player["Rarity"] == "Common":
            embed_color = 0x00d443
        elif player["Rarity"] == "Rare":
            embed_color = 0x8600d4
        elif player["Rarity"] == "Elite":
            embed_color = 0xd40000
        else:
            embed_color = 0xf1c40f


        keepOrSell = View()
        async def keep(interaction: discord.Interaction):
            if interaction.user != user:
                await interaction.followup.send("That's not your card!", ephemeral=True, delete_after=5)
                return
            db.add_card(ctx.author.id, player)
            
            await interaction.response.edit_message(
            content="✅ Card added to your collection!",
            view=None
            )

        async def sell(interaction: discord.Interaction):
            if interaction.user != user:
                await interaction.followup.send("That's not your card!", ephemeral=True, delete_after=5)
                return
            db.add_money(ctx.author.id, player['Price'])

            await interaction.response.edit_message(
            
            content=f"Card was sold for {player['Price']}",
            view=None
            )

        keepCard = Button(label="KEEP", style=discord.ButtonStyle.grey)
        keepCard.callback = keep

        sellCard = Button(label="SELL", style=discord.ButtonStyle.red)
        sellCard.callback = sell

        keepOrSell.add_item(keepCard)
        keepOrSell.add_item(sellCard)

        await slowOpen.delete()
        
        embed = discord.Embed(
            title=f"You got {player['Name']}!",
            description=f"Rarity: {player['Rarity']}\nRating: {player['Rating']}\nRole: {player['Role']}\nCountry: {player['Country']}\n\nPrice: {player['Price']}",
            color=embed_color,
        )

        await interaction.followup.send(embed=embed, view = keepOrSell) 



    OpenPack_Button = Button(label="Open Pack", style=discord.ButtonStyle.green)
    OpenPack_Button.callback = regularOpen

    FastOpen_Button = Button(label="Fast Open", style=discord.ButtonStyle.grey)
    FastOpen_Button.callback = button_callback
    

    view = View()
    view.add_item(OpenPack_Button)
    view.add_item(FastOpen_Button)

    probabilityMessage = discord.Embed(title="Pack Probabilities:")
    probabilityMessage.add_field(name="Common", value="50%", inline=False)
    probabilityMessage.add_field(name="Rare", value="  35%", inline=False)
    probabilityMessage.add_field(name="Elite", value="10%", inline=False)
    probabilityMessage.add_field(name="Legend", value=" 5%", inline=False)
    message = await ctx.send(
        embed=probabilityMessage,
        view=view
    )

@bot.command()
async def inv(ctx):
    use_id = ctx.author.id
    cards = db.get_cards(use_id)
    if not cards:
        await ctx.send("Your inventory is empty. Open some packs to get cards!", delete_after=5)
        return
    embed = discord.Embed(title=f"{ctx.author.name}'s Inventory", color=0x060f12)
    for card in cards:
        embed.add_field(name=card["Name"], value=f"Rarity: {card['Rarity']}", inline=False)
    await ctx.send(embed=embed)


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
    embed = discord.Embed(title="Balance Update",  description=f"{user.name}'s balance was andjusted by {amount}", color=0xff000 )
    await ctx.send(embed=embed)

bot.run(token)