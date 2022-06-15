#  Code created by Anthony Sheu on 5/2/22, 6:35 PM

import discord
from discord.ext import commands
import random
import time
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.get_channel(803717087980683264).send("antbot is online!")

@bot.listen('on_message')
async def listen(ctx):
    if ctx.author == bot.user: return
    if 'val' in ctx.content.lower(): await ctx.channel.send("<@597957202019352602> q comp")
    if 'brug' in ctx.content.lower(): await ctx.channel.send("i hate this game")
    if 'unfor' in ctx.content.lower(): await ctx.channel.send("truly")
    if 'kisorn' in ctx.content.lower(): await ctx.channel.send("ur bad")

@bot.command()
async def val(ctx, n=0):
    for i in range(n-1): await ctx.channel.send("<@597957202019352602> q comp"); time.sleep(0.6)

@bot.command()
async def spam(ctx, arg, n: int):
    if ctx.author == bot.user or n > 51: return
    for i in range(n): await ctx.send(arg)

@bot.command()
async def roll(ctx): await ctx.send(f"You rolled a {random.randint(1, 6)}!")

@bot.command()
async def flip(ctx): await ctx.send("The coin landed on heads!" if random.randint(0, 1) else "The coin landed on tails!")

@bot.command()
async def draw(ctx):
    face = {1: "diamonds", 2: "spades", 3: "hearts", 4: "clovers"}
    diff = {1: "ace of ", 11: "jack of ", 12: "queen of ", 13: "king of "}
    num = random.randint(1, 13)
    if num in [11, 12, 13]: await ctx.send("You drew a " + diff[num] + face[random.randint(1, 4)] + "!")
    elif num == 1: await ctx.send("You drew an " + diff[num] + face[random.randint(1, 4)] + "!")
    else: await ctx.send("You drew a " + repr(num) + " of " + face[random.randint(1, 4)] + "!")

bot.run('OTcwNzIyNzgwNDczNjAyMDg5.YnAGCg.Cp8OEzatZqhxMRkcEIgApPimeQo')
