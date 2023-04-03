
# Author: Jack Walker

# Init: IDK

# Description: Main run file for mechabridget something something


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import exceptions
import counter
import get_round
import tips_cmd
import value_cmd
import check_cmd
import last_cmd
import next_cmd
import suggestion_cmd
import ema_graph
import resetbot

load_dotenv()
  
# Bot variables
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=";", intents=intents)
token = os.getenv("TOKEN")

# Bot rich presence
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=";help"))
    print(f"Logged in as a bot {bot.user.name}")

# Reset Bot
@bot.command(pass_context=True, description="Provide this command with a UNIX Timestamp and the proper sheet name when a new event starts. Admins only")
@commands.has_permissions(administrator=True)
async def resetthebot(ctx, unix_timestamp, sheet_name):
    resetbot.resetrr(unix_timestamp, sheet_name)
    await ctx.send(
        f"> Event start has been set to <t:{unix_timestamp}>"
    )
    await ctx.send(
        f"> Sheet has been set to {sheet_name}"
    )



# Commands
#---------------------------------------------------------------------------



# Current Round Number | ;round
@bot.command(aliases=['r', 'rnd'], description="Displays the current round")
async def round(ctx):

    # Counter for ;round
    counter.addr(';round')

    await ctx.send(
        get_round.roundstr()
    )



# Closest Tips | ;tips <character> or 'all'
@bot.command(aliases=['t'], description="Displays the nearest tips")
async def tips(ctx, character):

    # Counter for ;tips
    counter.addr(';tips')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )
    else:
        await ctx.send(
            tips_cmd.tips_output(character)
        )



# Value of characters | ;value
@bot.command(aliases=['val', 'v'], description="Table of the most 'valuable' stonk based on current prices. Based on STD Deviation from the mean.")
async def value(ctx):

    # Counter for ;value
    counter.addr(';value')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )
    else:
        await ctx.send(
            value_cmd.value()
        )



# Check price in x rounds | ;check <# of rounds>
@bot.command(aliases=['ck'], description="Checks the highest growth between stonks between now and a given round")
async def check(ctx, hours):

    # Counter for ;check
    counter.addr(';check')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )

    else:
        await ctx.send(
            get_round.roundstr()
        )
        await ctx.send(
            check_cmd.check_output(hours)
        )



# Price Future Table | ;next <number of rounds> <character>
@bot.command(aliases=['n'], description="Table of next N rounds for a given stonk")
async def next(ctx, rounds, char):

    # Counter for ;next
    counter.addr(';next')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )
    
    else:
        await ctx.send(
            get_round.roundstr()
        )
        await ctx.send(
            next_cmd.next(rounds, char.lower())
        )



# Price History Table | ;last <number of rounds> <character>
@bot.command(aliases=['l'], description="Table of last N rounds for a given stonk")
async def last(ctx, rounds, char):

    # Counter for ;last
    counter.addr(';last')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )

    else:
        await ctx.send(
            get_round.roundstr()
        )
        await ctx.send(
            last_cmd.last(rounds, char.lower())
        )



# Purchase Suggestions for Current Round | ;suggest
@bot.command(aliases=['bb'], description="Purchase suggestion for the current round.")
async def bestbuy(ctx):

    # Counter for ;suggest
    counter.addr(';suggest')

    # Check for errors
    if exceptions.currentcheck():
        await ctx.send(
        f"> Prices for the current round have not been added yet! Please contact an editor."
        )

    else:
        await ctx.send(
            get_round.roundstr()
        )
        await ctx.send(
            suggestion_cmd.suggestion_cmd_output()
        )



# Exponential Moving Average Graph | ;ema
@bot.command(description="Graph of the Exponential Moving Average of a given stonk")
async def ema(ctx, character):

    # Counter for ;ema
    counter.addr(';ema')

    await ctx.send(file=discord.File((ema_graph.ema(character.lower()))))
    os.remove(character+'.png')



# Cloutzie only command to display runcounts of each command
@bot.command(description="Only for Clout")
async def statistics(ctx):
    if ctx.author.id == 328328717057392641:
        await ctx.send(
            counter.display()
        )
    else:
        await ctx.send('No Thanks!')



class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
            embed = discord.Embed(title="Bot help")
            # `mapping` is a dict of the bot's cogs, which map to their commands
            for cog, cmds in mapping.items():  # get the cog and its commands separately
                embed.add_field(
                    name = cog.qualified_name,       # get the cog name
                    value = f"{len(cmds)}  commands"  # get a count of the commands in the cog.
                )
                
            channel = self.get_destination()  # this method is inherited from `HelpCommand`, and gets the channel in context
            await channel.send(embed=embed)



# RUN THE BOT
bot.run(token)