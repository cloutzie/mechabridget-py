
import discord
import os
import random
from discord.ext import commands
import lsr_func
import bolband_func
import sma_func
import current_func
import ema_func
import last_func
import math_func
import tips_func
import roundtime_func
import afk_func
import bestbuy_func
import value_func
import next_function
  
bot = commands.Bot(command_prefix=";")
token = 'MTAzNzUzNDg5OTIzNTcyOTQzOQ.Gq57aK.vlXTdDj-sdYiq7smseFgDp6NxUXu9GW-Sml3w0'
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=";help"))
    print("Logged in as a bot {0.user}".format(bot))



###################

# LEAST SQUARED REGRESSION

@bot.command()
async def lsr(ctx, character):
    await ctx.send(file=discord.File((lsr_func.lsr(character.lower()))))
    os.remove(character+'.png')

###################

# BOLLINGER BAND (N/A)

@bot.command()
async def band(ctx, character):
    await ctx.send(file=discord.File((bolband_func.band(character.lower()))))
    os.remove(character+'.png')

###################

# SIMPLE MOVING AVERAGE

@bot.command()
async def sma(ctx, character):
    await ctx.send(file=discord.File((sma_func.sma(character.lower()))))
    os.remove(character+'.png')

###################

# EXPONENTIAL MOVING AVERAGE

@bot.command()
async def ema(ctx, character):
    await ctx.send(file=discord.File((ema_func.ema(character.lower()))))
    os.remove(character+'.png')

###################

# CURRENT PRICE OR ROUND #

@bot.command(aliases=['c', 'cur'])
async def current(ctx, character):
    if character == 'round':
        await ctx.send('> Current Round is ' + str(current_func.current('round')))
    else:
        await ctx.send('> ' + str(character.capitalize()) + ' Current Price is ' + str(current_func.current(character.lower())))

###################

# LAST 10 (N/A)

@bot.command()
async def last(ctx, rounds, character):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    await ctx.send(last_func.last(rounds, character.lower()))



@bot.command()
async def next(ctx, rounds, character):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    await ctx.send(next_function.next(rounds, character.lower()))
###################

# RANDOM MATH

@bot.command()
async def math(ctx, function, character, rounds):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    await ctx.send(math_func.math(function, character.lower(), rounds))

###################

# FIND NEXT TIP

@bot.command()
async def tips(ctx, character):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    if character in ['all', 'max']:
        for ch in ['celine', 'chocolat', 'fergus', 'lenny', 'lednas']:
            num, rounds = tips_func.tips(ch.lower())
            growth = round(((num / current_func.current(ch.lower()) - 1) * 100), 2)
            if (num != 0):
                await ctx.send('> ' + str(ch.capitalize()) + ' price will be ' + (str(int(num))) + ' on round ' + str(rounds) + ', for a growth of ' + str(growth) + '% between now and then')
            else:
                await ctx.send('> No Tips Available For ' + str(ch.capitalize()))
    else:
        num, rounds = tips_func.tips(character.lower())
        growth = round(((num / current_func.current(character.lower()) - 1) * 100), 2)
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
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    topgrow, topchar = afk_func.prcheck(hours)
    if len(topchar) > 0:
        await ctx.send('> ' + str(topchar.capitalize())  + ' will have the best known change of ' + str(topgrow) + '%' + ' in ' + str(hours) + ' hours on round ' + str(int(current_func.current('round')) + int(hours)))
    else:
        await ctx.send('> There are no tips available in ' + str(hours) + ' hours')

@bot.command(aliases=['bb', 'best'])
async def bestbuy(ctx):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
    topgrow, topchar, oneval, twoval, diff = bestbuy_func.bestbuy()
    if topchar == '':
        tgrow, tchar = afk_func.prcheck('2')
        await ctx.send('No tips for next round. Try ;value \n> ' + str(tchar.capitalize()) + ' will have the best known change of ' + str(tgrow) + '% 2 rounds from now.')
    elif (topgrow < 0) and (topgrow):
        tgrow, tchar = afk_func.prcheck('2')
        await ctx.send('> All characters with tips will decrease next round. Try ;value \n> ' + str(tchar.capitalize()) + ' will have the best known change of ' + str(tgrow) + '% 2 rounds from now.')
    elif len(topchar) > 2:
        await ctx.send('> ' + str(topchar.capitalize())  + ' is the best purchase on Round ' + str(current_func.current('round')) + ' ' + '[' + str(twoval) + '] with a growth of ' + str(topgrow) + '% ' + '[+' + str(diff) + '] to Round ' + str((current_func.current('round')) + 1) + ' [' + str(oneval) + ']')



@bot.command(aliases=['val', 'v'])
async def value(ctx):
    await ctx.send('> Current Round is ' + str(current_func.current('round')))
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

























# RUN THE BOT
bot.run(token)