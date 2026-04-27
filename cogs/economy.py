import discord
from discord.ext import commands
from discord.ui import Button, View

import time
from datetime import datetime, timedelta, UTC

import random

def setup(bot, db):
    #balance command to show the user's balance in an embed

    @bot.command()
    async def balance(ctx):
        user_id = ctx.author.id
        user_data = db.get_user(user_id)
        balance = user_data["balance"]
        embed = discord.Embed(title=f"{ctx.author.name}'s Balance", description=f"You have ${balance}💰", color=0x060f12)
        await ctx.send(embed=embed)
    
    #daily command to give the user a random amount of money between 850 and 1350, but only once every 24 hours
    @bot.command()
    async def daily(ctx):
        db.get_user(ctx.author.id) 
        data = db.load_data()
        user_id = str(ctx.author.id)
        today = datetime.now(UTC).date()

        if data[user_id].get("DailyClaim") == str(today):
            embed = discord.Embed(title="Daily Reward Already Claimed", description="You have already claimed your daily reward today. Come back tomorrow!", color=0xF50000)
            await ctx.send(embed=embed)
            return

        reward = random.randint(850, 1350)
        db.add_money(ctx.author.id, reward)
        data = db.load_data()
        data[user_id]["DailyClaim"] = str(today)
        db.save_data(data)

        embed = discord.Embed(title="Daily Reward Claimed!", description=f"You have received ${reward} as your daily reward. Come back tomorrow for more!", color=0x10F500)
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
        opened = user_data["Opened"]
        cards = len(user_data["cards"]) if user_data["cards"] else 0
        legendary_cards = sum(1 for card in user_data["cards"] if card["Rarity"] == "Legend") if user_data["cards"] else 0



        embed = discord.Embed(title=f"Profile Information", color=0x060f12)
        embed.add_field(name="\nLevel:", value=f"{level}", inline=False)
        embed.add_field(name="\nBalance:", value=f"${balance:,}", inline=False)
        embed.add_field(name="\nCards in Inventory:", value=f"{cards}", inline=False)
        embed.add_field(name="\nLegendary Cards:", value=f"{legendary_cards}", inline=False)
        embed.add_field(name="\nCards Opened:", value=f"{opened}", inline=False)


        await ctx.send(embed=embed)    

