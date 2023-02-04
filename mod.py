import discord
import discord
import json
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!',intents = discord.Intents.all(),activity=discord.Game(name="Minecraft"))
@bot.event
async def on_message(message):
    """ some on_message command """
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['fuck you', 'bitch','motherfucker','noob','not verry smart','go and fuck yourself']
    
    # delete curse word if match with the list
    if any(word in msg_content for word in curseWord):
        await message.delete()
        member = message.author
        await member.send(f"{member.mention}"'you have been muted for badword')
        role = member.guild.get_role(1069634546804461608)
        role1 = member.guild.get_role(1069168060168159262)
        await member.add_roles(role)
        await member.remove_roles(role1)
        await message.channel.send(f"{member.mention}"'has been muted! for bad word!')
bot.run('Token here')
