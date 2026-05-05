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
        AWPer = roaster["AWPer"]
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

    @bot.command()
    #Create a charecter limit
    async def setName(ctx, teamName):
        user = ctx.author.id
        db.get_user(user)
        data = db.load_data()
        data[str(user)]["Roaster"]["Name"] = teamName
        db.save_data(data)
        if len(teamName) > 10:
            embed = discord.Embed(title=f"Error :/", description="Charecter limit is 10.",color=0xF50000)
        else:
            embed = discord.Embed(title=f"Team name set to {teamName}!", color=0x060f12)
        await ctx.send(embed=embed)
    #make sure if player is already in team, to remove it and add new one
    @bot.command()
    async def setCoach(ctx, id: int):
        user = ctx.author.id
        data = db.load_data()
        user_data = data.get(str(user))
        id = id - 1

        if not user_data:
            embed = discord.Embed(title="Error", description="User not found.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        cards = user_data.get("cards", [])

        if id < 0 or id >= len(cards):
            embed = discord.Embed(title="Error", description="Invalid card ID.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        player = cards[id]

        if player["Role"] != "Coach":
            embed = discord.Embed(title="Error", description="This card is not a Coach.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        user_data["Roaster"]["Coach"] = player
        user_data['cards'].pop(id)
        db.save_data(data)

        embed = discord.Embed(
            title=f"Coach set to {player['Name']}!",
            color=0x060f12
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def setIGL(ctx, id: int):
        user = str(ctx.author.id)
        data = db.load_data()
        user_data = data.get(user)
        id = id - 1

        if not user_data:
            await ctx.send(embed=discord.Embed(title="Error", description="User not found.", color=0xF50000))
            return

        cards = user_data.get("cards", [])

        if id < 0 or id >= len(cards):
            await ctx.send(embed=discord.Embed(title="Error", description="Invalid card ID.", color=0xF50000))
            return

        player = cards[id]

        if player["Role"] != "IGL":
            await ctx.send(embed=discord.Embed(title="Error", description="This card is not an IGL.", color=0xF50000))
            return

        data[user]["Roaster"]["IGL"] = player
        data[user]["cards"].pop(id)
        db.save_data(data)

        await ctx.send(embed=discord.Embed(title=f"IGL set to {player['Name']}!", color=0x060f12))
    
    @bot.command()
    async def setAWP(ctx, id: int):
        user = str(ctx.author.id)
        data = db.load_data()
        user_data = data.get(user)
        id = id - 1

        if not user_data:
            await ctx.send(embed=discord.Embed(title="Error", description="User not found.", color=0xF50000))
            return

        cards = user_data.get("cards", [])

        if id < 0 or id >= len(cards):
            await ctx.send(embed=discord.Embed(title="Error", description="Invalid card ID.", color=0xF50000))
            return

        player = cards[id]

        if player["Role"] != "AWPer":
            await ctx.send(embed=discord.Embed(title="Error", description="This card is not an AWPer.", color=0xF50000))
            return

        data[user]["Roaster"]["AWPer"] = player
        data[user]["cards"].pop(id)
        db.save_data(data)

        await ctx.send(embed=discord.Embed(title=f"AWPer set to {player['Name']}!", color=0x060f12))

    @bot.command()
    async def setRifler(ctx, id: int):
        user = str(ctx.author.id)
        data = db.load_data()
        user_data = data.get(user)
        id = id - 1

        if not user_data:
            embed = discord.Embed(title="Error", description="User not found.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        cards = user_data.get("cards", [])

        if id < 0 or id >= len(cards):
            embed = discord.Embed(title="Error", description="Invalid card ID.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        player = cards[id]

        if player["Role"] != "Rifler":
            embed = discord.Embed(title="Error", description="This card is not a Rifler.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        roaster = user_data["Roaster"]
        riflers = roaster["Rifelrs"]

        if len(riflers) >= 3:
            embed = discord.Embed(title="Error", description="You can only have 3 Riflers in your team.", color=0xF50000)
            await ctx.send(embed=embed)
            return

        riflers.append(player)
        user_data['cards'].pop(id)
        db.save_data(data)

        embed = discord.Embed(
            title=f"Rifler {player['Name']} added to your team!",
            color=0x060f12
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def clearRoaster(ctx):
        user = str(ctx.author.id)
        data = db.load_data()   
        data[str(user)]["cards"].append(data[str(user)]["Roaster"]["Coach"]) if data[str(user)]["Roaster"]["Coach"] else None
        data[str(user)]["cards"].append(data[str(user)]["Roaster"]["IGL"]) if data[str(user)]["Roaster"]["IGL"] else None
        data[str(user)]["cards"].append(data[str(user)]["Roaster"]["AWPer"]) if data[str(user)]["Roaster"]["AWPer"] else None
        for rifler in data[str(user)]["Roaster"]["Rifelrs"]:
            data[str(user)]["cards"].append(rifler)
        data[str(user)]["Roaster"]["Coach"] = None
        data[str(user)]["Roaster"]["IGL"] = None
        data[str(user)]["Roaster"]["AWPer"] = None
        data[str(user)]["Roaster"]["Rifelrs"] = []
        db.save_data(data)
        embed = discord.Embed(title="Team cleared!", description="Your team has been cleared. You can start building a new one!", color=0x060f12)
        await ctx.send(embed=embed)