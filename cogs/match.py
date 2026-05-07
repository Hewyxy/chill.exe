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
        await asyncio.sleep(1)
        #Match Logic (Beta) might will need an update in future
        userTeam = user_roaster.copy()
        enemyTeam = enemy_data["Roaster"].copy()

        userCoach = userTeam["Coach"]
        userIGL = userTeam["IGL"]
        userAWP = userTeam["AWPer"]
        userRifflers = userTeam["Rifelrs"]

        enemyCoach = enemyTeam["Coach"]
        enemyIGL = enemyTeam["IGL"]
        enemyAWP = enemyTeam["AWPer"]
        enemyRifflers = enemyTeam["Rifelrs"]

        userAVGpower = (userIGL["Rating"] + userAWP["Rating"] + userRifflers[0]["Rating"] + userRifflers[1]["Rating"] + userRifflers[2]["Rating"])*(1 + (userCoach["Rating"]/100))
        enemyAVGpower = (enemyIGL["Rating"] + enemyAWP["Rating"] + enemyRifflers[0]["Rating"] + enemyRifflers[1]["Rating"] + enemyRifflers[2]["Rating"])*(1 + (enemyCoach["Rating"]/100))

        totalPower = userAVGpower + enemyAVGpower

        userScore = 0
        enemyScore = 0

        embed.title = f"{userTeam['Name']:>11} vs {enemyTeam['Name']:>11}"
        embed.description = f"```\nScore: {userScore} : {enemyScore}\n```"
        embed.add_field(name="Last Rounds", value="```\nMatch starting...\n```", inline=False) 
        await message.edit(embed=embed)

        round_history=[]
        round = 0
        maxRound = 13
        while userScore < maxRound and enemyScore < maxRound:
            num = random.randint(0, int(totalPower))
            if round == 12:
                round_history.append(f"Switching sides!")
                embed.color = 0xF5C000
            elif userScore == (maxRound-1) and enemyScore == (maxRound-1):
                round_history.append(f"Overtime!")
                maxRound +=3
                embed.color = 0xF5C000
            elif num <= userAVGpower:
                userScore += 1
                embed.color = 0x00F508
                round_history.append(f"{userTeam['Name']} wins round!")
            else:
                enemyScore += 1
                embed.color = 0xF50000
                round_history.append(f"{enemyTeam['Name']} wins round!")

            last_rounds = "\n".join(round_history[-7:])

            embed.description = f"```\nScore: {userScore} : {enemyScore}\n```"
            embed.set_field_at(0, name="Last Rounds", value=f"```\n{last_rounds}\n```", inline=False)

            round += 1

            await asyncio.sleep(2)
            await message.edit(embed=embed)
        if userScore > enemyScore:
            data[user]["Roaster"]["Points"] += 5
            data[user]["balance"] += 50
            embed = discord.Embed(title=f"Congrats you won {enemyTeam['Name']}!", description=f"You earned: $50 and 5 VRS points!", color=0x41F500)
        else:
            lost = 0
            if user_roaster["Points"] >= 5:
                lost = 5
                user_roaster["Points"] -= 5
            embed = discord.Embed(title=f"You lost to {enemyTeam['Name']} :(", description=f"You lost {lost} VRS points.", color=0xF50000)
        db.save_data(data)
        await message.edit(embed=embed)

                    






