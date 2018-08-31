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
    if server == "ttt":
        await bot.say("<@%s> | Connect to our TTT server with: steam://connect/ttt.erasegaming.com:27065" % (ctx.message.author.id))
    elif server == "discord":
        await bot.say("<@%s> | Connect to our Discord server with: https://discord.gg/JpgEJPV" % (ctx.message.author.id)) 

@bot.command(pass_context = True)
async def dice(ctx):
    result = str(random.randint(1, 6))
    await bot.say("<@%s> | Dice Roll: " % (ctx.message.author.id) + result) 
        
@bot.command(pass_context = True)
async def flip(ctx):
    result = random.randint(1, 2)
    if result == 1:
        await bot.say("<@%s> | Coinflip: heads" % (ctx.message.author.id))
    else:
        await bot.say("<@%s> | Coinflip: tails" % (ctx.message.author.id))

@bot.command(pass_context = True)
async def forum(ctx):
    await bot.say("<@%s> | Visit our forums at: https://www.erasegaming.com" % (ctx.message.author.id))

@bot.command(pass_context = True)
async def forums(ctx):
    await bot.say("<@%s> | Visit our forums at: https://www.erasegaming.com" % (ctx.message.author.id)) 

@bot.command(pass_context = True)
async def randomnum(ctx, rmin: int, rmax: int):
    result = random.randint(rmin, rmax)
    rmin = str(rmin)
    rmax = str(rmax)
    result = str(result)
    userid = ctx.message.author.id
    await bot.say("<@%s> | Random number between " % (userid) + rmin + " and " + rmax + ": " + result)

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
    await bot.http.delete_message(ctx.message.channel.id, ctx.message.id)
    with open('anime.png', 'rb') as image:
        await bot.send_file(discord.Object(id = channelid), image)

@bot.command(pass_context = True)
async def ooga(ctx):
    await bot.http.delete_message(ctx.message.channel.id, ctx.message.id)
    await bot.say("<@%s> Ooga Booga" % (ctx.message.author.id))
    
@bot.command(pass_context = True)
async def piggie(ctx):
    await bot.http.delete_message(ctx.message.channel.id, ctx.message.id)
    await bot.say("Oink Oink <@%s>" % ("151802030984265729"))
        
@bot.command(pass_context = True)
async def yee(ctx):
    await bot.http.delete_message(ctx.message.channel.id, ctx.message.id)
    with open('yee.png', 'rb') as image:
        await bot.send_file(discord.Object(id = channelid), image)
    
bot.run("") #Bot Token
