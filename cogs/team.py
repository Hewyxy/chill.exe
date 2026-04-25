import discord
from discord.ext import commands
from discord.ui import Button, View

def setup(bot, db):
    #Team command to set the user's team with a name, points, coach, IGL, AWPer, and 3 riflers,
    #  and show the team in an embed, with different colors for different points ranges
    @bot.command()
    async def team(ctx):
        user = ctx.author.id
        user_data = db.get_user(user)
        roaster = user_data["Roaster"]
        teamName = roaster["Name"]
        teamPoints = roaster["Points"]
        coach = roaster["Coach"]
        iGL = roaster["IGL"]
        AWPer = roaster["AWper"]
        riflers = roaster["Rifelrs"]

        power = coach["Rating"] if coach else 0
        power += iGL["Rating"] if iGL else 0
        power += AWPer["Rating"] if AWPer else 0
        power += sum(rifler["Rating"] for rifler in riflers) if riflers else 0
        embed = discord.Embed(title=f"[{teamPoints}] {teamName}", color=0x060f12)
        embed.add_field(name="Coach:", value=coach["Name"] if coach else "Not set", inline=False)
        embed.add_field(name="IGL:", value=iGL["Name"] if iGL else "Not set", inline=False)
        embed.add_field(name="AWPer:", value=AWPer["Name"] if AWPer else "Not set", inline=False)
        embed.add_field(name="Riflers:", value="\n".join(r["Name"] for r in riflers) if riflers else "Not set", inline=False)
        embed.add_field(name="\nPower:", value=f"{power:.2f}", inline=False)

        await ctx.send(embed=embed)
