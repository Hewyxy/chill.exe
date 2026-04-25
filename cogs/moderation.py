import discord
from discord.ext import commands
from discord.ui import Button, View

def setup(bot, db):
    #Command Help
    @bot.command()
    async def helpme(ctx):
        embed = discord.Embed(title="Command Help", description="List of available commands:", color=0x060f12)
        embed.add_field(name="!helpme", value="Shows the list of commands.", inline=False)
        embed.add_field(name="!profile", value="Displays your profile and stats.", inline=False)

        embed.add_field(name="!joke", value="Fetches a random dark joke.", inline=False)
        embed.add_field(name="!sound", value="Plays a sound in your current voice channel.", inline=False)

        embed.add_field(name="!balance", value="Shows your current balance.", inline=False)
        embed.add_field(name="!daily", value="Claim your daily reward.", inline=False)

        embed.add_field(name="!inv", value="Displays your card inventory.", inline=False)
        embed.add_field(name="!sell <number>", value="Sells a card by its number.", inline=False)
        embed.add_field(name="!sell all", value="Sells all cards except legendary ones.", inline=False)

        embed.add_field(name="!clear <amount>", value="Clears a specified number of messages (max 500). Requires Manage Messages permission.", inline=False)
        await ctx.send(embed=embed)
        
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