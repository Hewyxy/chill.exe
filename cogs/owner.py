import discord
from discord.ext import commands
from discord.ui import Button, View

def setup(bot, db):
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
        embed = discord.Embed(title="Balance Update",  description=f"{user.name}'s balance was adjusted by {amount}", color=0x10F500)
        await ctx.send(embed=embed)

    @bot.command()
    @commands.is_owner()
    async def getdb(ctx):
        user = await bot.fetch_user(449584926359158789)
        await user.send(
            content="📦 ЭКСТРЕНЫЙ БЭКАП!!!",
            file=discord.File("database.json")
        )