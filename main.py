#Setting up Discord Library and Bot
import asyncio
import db
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
from discord import activity, ActivityType
from discord.ext import tasks
# Other imports
import os
import random
from cardPacks import openRegularPack, openIGLPack, openAWPPack

#sETTING UP THE BOT
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

load_dotenv()
token = os.getenv("DISCORD_TOKEN") 

from cogs import fun, match, owner, moderation, economy, cards, team
owner.setup(bot, db)
moderation.setup(bot, db)
economy.setup(bot, db)
cards.setup(bot, db)
fun.setup(bot, db)
team.setup(bot, db)
#match.setup(bot, db)

@bot.event
async def on_ready():
    await bot.tree.sync()
    backup_database.start() 
    print("Slash commands synced")
    print(f'Logged in as {bot.user}')
    activity = discord.Activity(type=discord.ActivityType.playing, name="We are in beta, use !helpme for commands")
    thoughts = discord.Activity(type=discord.ActivityType.listening, name="the sound of the server growing")
    await bot.change_presence(activity=activity)
    print("Activity set")

    user = await bot.fetch_user(449584926359158789)
    await user.send("✅ Бот запущен!")
    


@bot.event
async def error(event, *args, **kwargs):
    import traceback
    print(traceback.format_exc())

#clearing any errors that may occur with the clear command
@bot.event
# Handle command errors globally
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            'This command does not exist. Use !helpme to see the list of available commands',

            delete_after=5
        )
@bot.event
async def on_error(event, *args, **kwargs):
    import traceback
    print(traceback.format_exc())
# Handle errors specific to the clear command

OWNER_ID = 449584926359158789

@tasks.loop(hours=24)
async def backup_database():
    user = await bot.fetch_user(OWNER_ID)
    await user.send(
        content="📦 Автобэкап базы данных",
        file=discord.File("database.json")
    )


bot.run(token)