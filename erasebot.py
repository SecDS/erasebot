import async
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("EraseBot online")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = "User")
    await bot.add_roles(member, role)

'''
@bot.event
async def on_message(message):
    print("[MESSAGE] " + str(message.author) + "(" + str(message.author.id) + ") sent the message \"" + str(message.content) + "\"")
'''

@bot.command(pass_context = True)
async def connect(ctx, server: str):
    server = server.lower()
    userid = ctx.message.author.id
    if server == "ttt":
        await bot.say("<@%s> | Connect to our TTT server with: steam://connect/ttt.erasegaming.com:27065" % (userid))
    elif server == "discord":
        await bot.say("<@%s> | Connect to our Discord server with: https://discord.gg/JpgEJPV" % (userid)) 

@bot.command(pass_context = True)
async def dice(ctx):
    result = random.randint(1, 6)
    result = str(result)
    userid = ctx.message.author.id
    await bot.say("<@%s> | Dice Roll: " % (userid) + result) 
        
@bot.command(pass_context = True)
async def flip(ctx):
    result = random.randint(1, 2)
    userid = ctx.message.author.id
    if result == 1:
        await bot.say("<@%s> | Coinflip: heads" % (userid))
    elif result == 2:
        await bot.say("<@%s> | Coinflip: tails" % (userid))

@bot.command(pass_context = True)
async def forum(ctx):
    userid = ctx.message.author.id
    await bot.say("<@%s> | Visit our forums at: https://www.erasegaming.com" % (userid))

@bot.command(pass_context = True)
async def forums(ctx):
    userid = ctx.message.author.id
    await bot.say("<@%s> | Visit our forums at: https://www.erasegaming.com" % (userid)) 

@bot.command(pass_context = True)
async def randomnum(ctx, rmin: int, rmax: int):
    result = random.randint(rmin, rmax)
    rmin = str(rmin)
    rmax = str(rmax)
    result = str(result)
    userid = ctx.message.author.id
    await bot.say("<@%s> | Random number between " % (random_userid) + random_min + " and " + random_max + ": " + random_result)

@bot.command(pass_context = True)
async def staff(ctx):
    role_table = []
    for member in ctx.message.server.members:
        for role in member.roles:
            if role.name == "Owner" or "Co-Owner" or "Super Admin" or "Admin" or "Moderator" or "Operator":
                role_table.append([role.name, member.name])
    for element in role_table:
        await bot.say(element[1] + " | " + element[2])

@bot.command(pass_context = True)
async def anime(ctx):
    channelid = ctx.message.channel.id
    messageid = ctx.message.id
    await bot.http.delete_message(channelid, messageid)
    with open('anime.png', 'rb') as image:
        await bot.send_file(discord.Object(id = channelid), image)

@bot.command(pass_context = True)
async def ooga(ctx):
    channelid = ctx.message.channel.id
    messageid = ctx.message.id
    userid = ctx.message.author.id
    await bot.http.delete_message(channelid, messageid)
    await bot.say("<@%s> Ooga Booga" % (userid))
    
@bot.command(pass_context = True)
async def piggie(ctx):
    channelid = ctx.message.channel.id
    messageid = ctx.message.id
    await bot.http.delete_message(channelid, messageid)
    await bot.say("Oink Oink <@%s>" % ("151802030984265729"))
        
@bot.command(pass_context = True)
async def yee(ctx):
    channelid = ctx.message.channel.id
    messageid = ctx.message.id
    await bot.http.delete_message(channelid, messageid)
    with open('yee.png', 'rb') as image:
        await bot.send_file(discord.Object(id = channelid), image)
    
bot.run("") #Bot Token
