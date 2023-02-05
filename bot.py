import discord
from discord.ext import commands
from discord.utils import get
import os
import datetime
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
arg = 1
channel = bot.get_channel(1071416735909036154)


@bot.event
async def on_ready():
    channel = bot.get_channel(1071757524941951037)
    activity = discord.Activity(
        name='Minecraft', type=discord.ActivityType.playing, large_image='lol', large_text='Yes')
    await bot.change_presence(activity=activity)
    await channel.send('Bot online')


async def on_error():
    channel = bot.get_channel(1071757524941951037)
    await channel.send('error')


async def on_guild_join(guild):
    channel = bot.get_channel(1071757524941951037)
    await channel.send("Wassup! welcome ")


@bot.listen('on_message')
async def lol(message):
    """ some on_message command """
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['fuck you', 'bitch', 'motherfucker',
                 'noob', 'not verry smart', 'go and fuck yourself']

    # delete curse word if match with the list
    if any(word in msg_content for word in curseWord):
        await message.delete()
        member = message.author
        await member.send(f"{member.mention}"'you have been muted for badword')
        await member.timeout(datetime.timedelta(minutes=10))

        await message.channel.send(f"{member.mention}"'has been muted! for bad word!')


@bot.command()
async def website(ctx):
    await ctx.channel.send('https://github.com/MichaelonGit/bot')


@bot.command()
async def mute(ctx, member: discord.Member,minutes:int):
    member1 = ctx.message.author
    if ctx.author.top_role.permissions.administrator == True:
        if minutes >= 1:
            member1 = ctx.message.author
            await member.timeout(datetime.timedelta(minutes=minutes))
            print('yes', member)
            yes = minutes
            await ctx.channel.send(f"{member1.mention}"'has muted'f"{member.mention}" )
        else:
            await ctx.reply(member1.mention + ' has removed some minutes ' + ' from ' + member.mention)
    else:
        await ctx.channel.send('404 Permission not found :(')


@bot.command()
async def list(ctx, message):
    if ctx.author.top_role.permissions.administrator == True:
        if message == 'admin':
            member = ctx.message.author
            yes = f"{member.mention}"
            sus = 'admin commands : `!list admin` and `!mute <user with tag>`'
            await member.send(yes)
            await member.send(sus)
            await ctx.reply(f"{member.mention}"'look in your dms!')
            await ctx.message.delete()
        else:
            embed = discord.Embed(title="Help:", url="https://github.com/MichaelonGit/bot",
                                  description="Evry command is here", color=0xFF5733)
            await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="Help:", url="https://github.com/MichaelonGit/bot",
                              description="Evry command is here", color=0xFF5733)
        await ctx.reply(embed=embed)


@bot.command()
async def error(ctx):
    await ctx.send('somthing went wrong||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://myfilesigusse.tixte.co/error.mp4')


@bot.command()
async def github(ctx):
    embed = discord.Embed(title="My github page:", url="https://github.com/MichaelonGit/bot",
                          description="My gitub is not new lol", color=0xce0d0d)
    embed.set_author(name="Michael9Gamer", url="https://github.com/MichaelonGit/bot",
                     icon_url="https://myfilesigusse.tixte.co/linux.png")
    embed.set_thumbnail(url="https://myfilesigusse.tixte.co/linux.png")
    embed.set_footer(text="lol")
    await ctx.reply(embed=embed)


@bot.command()
async def mail(ctx, member: discord.Member, *, msg):
    member1 = ctx.message.author
    await ctx.message.delete()
    await member.send(msg + "" + ' | ' + f"{member1.mention}" + ' send you a message')


@bot.command()
async def kick1(ctx, member: discord.Member):
    admin = member.guild.get_member(831904772721868900)
    if ctx.author.top_role.permissions.administrator == True:
        await member.kick()
    else:
        await ctx.reply(member.mention + 'you are trying to kick?' + admin.mention)


@bot.command()
async def support(ctx):
    await ctx.reply('https://discord.gg/SWVwQqZ4vK')
@bot.command()
async def nevergonnagiveyouup(ctx):
    await ctx.reply('Never gonna give you up!||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://www.youtube.com/watch?v=dQw4w9WgXcQ')
bot.run('token')
