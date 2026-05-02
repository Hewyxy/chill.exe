import discord
from discord.ext import commands
from discord.ui import Button, View
import random
import asyncio

def setup(bot, db):
    @bot.command()
    async def play(ctx):
        user = str(ctx.author.id)
        data = db.load_data()
        user_data = db.get_user(ctx.author.id)
        user_roaster = user_data["Roaster"]

        embed = discord.Embed(title="Matchmaking", description="Finding a match for you", color=0x060f12)
        message = await ctx.send(embed=embed)
        count = 0
        reset = 3

        while count < 8:
            if count == reset:
                embed.description = "Finding a match for you"
                reset += 3
                await message.edit(embed=embed)
            await asyncio.sleep(.5)
            embed.description += "."
            await message.edit(embed=embed)
            count += 1

        if not user_roaster["IGL"] or not user_roaster["AWPer"] or not user_roaster["Rifelrs"] or len(user_roaster["Rifelrs"]) < 3:
            await ctx.send(embed=discord.Embed(title="Incomplete Roaster", description="You need IGL, AWPer and 3 Riflers.", color=0xF50000))
            return

        opponents = [
            uid for uid in data if uid != user
            and data[uid].get("Roaster", {}).get("IGL")
            and data[uid].get("Roaster", {}).get("AWPer")
            and len(data[uid].get("Roaster", {}).get("Rifelrs", [])) >= 3
        ]

        if not opponents:
            await ctx.send(embed=discord.Embed(title="No Opponents Found :(", description="No players with complete roasters found.", color=0xF50000))
            return

        enemy_id = random.choice(opponents)
        enemy_data = db.get_user(enemy_id)

        

        embed = discord.Embed(title="Match Found!", description=f"You matched against **{enemy_data['Roaster']['Name']}**!", color=0x10F500)
        await message.edit(embed=embed)
        #keep writing logic of the match here




