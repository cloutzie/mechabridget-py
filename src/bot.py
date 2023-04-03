
# Author: Jack Walker

# Init: IDK

# Description: Main run file for mechabridget something something


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import counter
import get_round
import last_cmd
import next_cmd
import suggestion_cmd
import lsr_graph
import sma_graph
import ema_graph

load_dotenv()
  
# Bot variables
bot = commands.Bot(command_prefix=";")
token = os.getenv("TOKEN")

# Bot rich presence
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=";help"))
    print(f"Logged in as a bot {bot.user.name}")



# Commands
#---------------------------------------------------------------------------



# Current Round Number | ;round
@bot.command(aliases=['r', 'rnd'])
async def round(ctx):

    # Counter for ;round
    counter.addr(';round')

    await ctx.send(
        get_round.roundstr()
    )



# Price Future Table | ;next <number of rounds> <character>
@bot.command(aliases=['n'])
async def next(ctx, rounds, char):

    # Counter for ;next
    counter.addr(';next')
    
    await ctx.send(
        get_round.roundstr()
    )
    await ctx.send(
        next_cmd.next(rounds, char.lower())
    )



# Price History Table | ;last <number of rounds> <character>
@bot.command(aliases=['l'])
async def last(ctx, rounds, char):

    # Counter for ;last
    counter.addr(';last')

    await ctx.send(
        get_round.roundstr()
    )
    await ctx.send(
        last_cmd.last(rounds, char.lower())
    )



# Purchase Suggestions for Current Round | ;suggest
@bot.command(aliases=['sg'])
async def suggest(ctx):

    # Counter for ;suggest
    counter.addr(';suggest')

    await ctx.send(
        get_round.roundstr()
    )
    await ctx.send(
        suggestion_cmd.suggestion_cmd_output()
    )



# Least Squared Regression Graph | ;lsr
@bot.command()
async def lsr(ctx, character):

    # Counter for ;lsr
    counter.addr(';lsr')

    await ctx.send(file=discord.File((lsr_graph.lsr(character.lower()))))
    os.remove(character+'.png')



# Simple Moving Average Graph | ;sma
@bot.command()
async def sma(ctx, character):

    # Counter for ;sma 
    counter.addr(';sma')

    await ctx.send(file=discord.File((sma_graph.sma(character.lower()))))
    os.remove(character+'.png')



# Exponential Moving Average Graph | ;ema
@bot.command()
async def ema(ctx, character):

    # Counter for ;ema
    counter.addr(';ema')

    await ctx.send(file=discord.File((ema_graph.ema(character.lower()))))
    os.remove(character+'.png')



@bot.command()
async def statistics(ctx):
    if ctx.author.id == 328328717057392641:
        await ctx.send(
            counter.display()
        )
    else:
        await ctx.send('No Thanks!')


'''###################


# FIND NEXT TIP

@bot.command()
async def tips(ctx, character):
    await ctx.send('> Current Round is ' + str(get_round.current('round')))
    if character in ['all', 'max']:
        for ch in ['celine', 'chocolat', 'fergus', 'lenny', 'lednas']:
            num, rounds = tips_func.tips(ch.lower())
            growth = round(((num / get_round.current(ch.lower()) - 1) * 100), 2)
            if (num != 0):
                await ctx.send('> ' + str(ch.capitalize()) + ' price will be ' + (str(int(num))) + ' on round ' + str(rounds) + ', for a growth of ' + str(growth) + '% between now and then')
            else:
                await ctx.send('> No Tips Available For ' + str(ch.capitalize()))
    else:
        num, rounds = tips_func.tips(character.lower())
        growth = round(((num / get_round.current(character.lower()) - 1) * 100), 2)
        if (num != 0):
            await ctx.send('> ' + str(character.capitalize()) + ' price will be ' + (str(int(num))) + ' on round ' + str(rounds) + ', for a growth of ' + str(growth) + '% between now and then')
        else:
            await ctx.send('> No Tips Available For ' + str(character.capitalize()))
###################

# FIND LOCAL TIME AT GIVEN ROUND #

@bot.command(aliases=['rt', 'time'])
async def roundtime(ctx, round):
    await ctx.send('> Round ' + str(round) + ' will begin at <t:' + str(roundtime_func.roundtime(round)) + ':f>')

###################

# FIND OPTIMAL PURCHASE WITH GIVEN  AFK HOURS

@bot.command(aliases=['prc', 'check'])
async def prcheck(ctx, hours):
    await ctx.send('> Current Round is ' + str(get_round.current('round')))
    topgrow, topchar = afk_func.prcheck(hours)
    if len(topchar) > 0:
        await ctx.send('> ' + str(topchar.capitalize())  + ' will have the best known change of ' + str(topgrow) + '%' + ' in ' + str(hours) + ' hours on round ' + str(int(get_round.current('round')) + int(hours)))
    else:
        await ctx.send('> There are no tips available in ' + str(hours) + ' hours')

@bot.command(aliases=['bb', 'best'])
async def bestbuy(ctx):
    await ctx.send('> Current Round is ' + str(get_round.current('round')))
    topgrow, topchar, oneval, twoval, diff = bestbuy_func.bestbuy()
    if topchar == '':
        tgrow, tchar = afk_func.prcheck('2')
        await ctx.send('No tips for next round. Try ;value \n> ' + str(tchar.capitalize()) + ' will have the best known change of ' + str(tgrow) + '% 2 rounds from now.')
    elif (topgrow < 0) and (topgrow):
        tgrow, tchar = afk_func.prcheck('2')
        await ctx.send('> All characters with tips will decrease next round. Try ;value \n> ' + str(tchar.capitalize()) + ' will have the best known change of ' + str(tgrow) + '% 2 rounds from now.')
    elif len(topchar) > 2:
        await ctx.send('> ' + str(topchar.capitalize())  + ' is the best purchase on Round ' + str(get_round.current('round')) + ' ' + '[' + str(twoval) + '] with a growth of ' + str(topgrow) + '% ' + '[+' + str(diff) + '] to Round ' + str((get_round.current('round')) + 1) + ' [' + str(oneval) + ']')



@bot.command(aliases=['val', 'v'])
async def value(ctx):
    await ctx.send('> Current Round is ' + str(get_round.current('round')))
    await ctx.send(value_func.value())



@bot.command()
async def echo(ctx, phrase):
    if ctx.author.id == 328328717057392641:
        await ctx.send(phrase)
    else:
        await ctx.send('No Thanks!')

@bot.command()
async def help(ctx):
    await ctx.send('https://docs.google.com/document/d/1eSHahCHM9U09vTj_f57-3eX99m3xTh0K0cCW-5_mVO8/edit?usp=sharing')
        
@bot.command()
async def sheet(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/18_E4zHHakFvRqdtsVJvrjOPb4F-cfGpvAKFdxIxBXLY/edit?usp=sharing')

@bot.command(aliases=['exmath', 'exbuy', 'experimental', 'exafk'])
async def exp(ctx, choice='', rounds=''):
    await ctx.send('This command doesnt work right now; try using ;value')

@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=1037534899235729439&permissions=8&scope=bot%20applications.commands')
###################

'''























# RUN THE BOT
bot.run(token)