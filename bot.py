import discord
from discord.ext import commands
from discord.utils import get
import os

bot = commands.Bot(command_prefix='!',intents = discord.Intents.all())
arg=1
channel = bot.get_channel(1071416735909036154)
@bot.event
async def on_ready():
    channel = bot.get_channel(name='botlog')
    activity = discord.Activity(name='Minecraft', type=discord.ActivityType.playing,large_image='lol', large_text='Yes')
    await bot.change_presence(activity=activity)
    await channel.send('Bot online')
async def on_error():
    error()
@bot.command()
async def website(ctx):
    await ctx.channel.send('https://github.com/MichaelonGit/bot')
@bot.command()
async def unmute(ctx,member: discord.Member):
    if ctx.author.top_role.permissions.administrator == True:
        role = member.guild.get_role(1069634546804461608)
        member1 = ctx.message.author
        await member.remove_roles(role)
        await ctx.channel.send(f"{member1.mention}"'has unmuted'f"{member.mention}")
    else:
        await ctx.channel.send('404 Permission not found :(')
@bot.command()
async def mute(ctx,member: discord.Member):
    if ctx.author.top_role.permissions.administrator == True:
        member1 = ctx.message.author
        role = member.guild.get_role(1069634546804461608)
        role1 = member.guild.get_role(1069168060168159262)
        await member.add_roles(role)
        await member.remove_roles(role1)
        print('yes',member)
        await ctx.channel.send(f"{member1.mention}"'has muted'f"{member.mention}")
        
    else:
        await ctx.channel.send('404 Permission not found :(')
@bot.command()
async def minserverip(ctx):
    member= ctx.message.author
    hostname = 'https://github.com/MichaelonGit/bot'
    response = os.system("ping -c 1 " + hostname + ' 2>/dev/null 1>&2')
    if response == 0:
        await ctx.send(member.mention + " " + hostname + ' is currently online')
    else:
        await ctx.send(member.mention + " " + hostname + ' is down')
    await ctx.channel.send('https://github.com/MichaelonGit/bot')
    await ctx.send(f"{member.mention}")
@bot.command()
async def list(ctx,message):
    if ctx.author.top_role.permissions.administrator == True:
        if message == 'admin':
            member = ctx.message.author
            yes = f"{member.mention}"
            sus ='admin commands : `!list admin` and `!mute <user with tag>`'
            await member.send(yes)
            await member.send(sus)
            await ctx.send(f"{member.mention}"'look in your dms!')
            
        else:
            embed=discord.Embed(title="Help:", url="https://sites.google.com/view/the-bot/startseite", description="Evry command is here", color=0xFF5733)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Help:", url="https://sites.google.com/view/the-bot/startseite", description="Evry command is here", color=0xFF5733)
        await ctx.send(embed=embed)
@bot.command()
async def ping(ctx,arg):
    hostname = arg
    member = ctx.message.author
    response = os.system("ping -c 1 " + hostname + ' 2>/dev/null 1>&2')
    if response == 0:
        await ctx.send(member.mention + " " + hostname + ' is up')
    else:
        await ctx.send(member.mention + " " + hostname + ' is down')
@bot.command()
async def error(ctx):
    await ctx.send('somthing went wrong||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://myfilesigusse.tixte.co/error.mp4')

bot.run('Token insert here')
