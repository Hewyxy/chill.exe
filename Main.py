#Setting up Discord Library and Bot
import asyncio

import discord
from discord.ext import commands

# Other imports
import os
import time

#sETTING UP THE BOT
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

#Command Help
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="!joke", value="Fetches a random dark joke.", inline=False)
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

#clearing any errors that may occur with the clear command
@bot.event
# Handle command errors globally
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            'This command does not exist. Use !help to see the list of available commands',
            delete_after=5
        )
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


