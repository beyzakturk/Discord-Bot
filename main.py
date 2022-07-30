import discord
from discord.ext import commands
from utils import *
from functions import *

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

Bot = commands.Bot(command_prefix='!hcm ', intents=intents)

game = Game()


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="neye-baktin-aslan")
    await channel.send(f"{member} neden geldin. Umarım eli boş gelmemişsindir!")  # Sonucu discord ekranından değil terminalden de görmek istersek await kullanılır.


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channel, name="neye-baktin-aslan")
    await channel.send(f"{member} yolun açık olsun. Zararın oldu ise iki elim yakanda!")


@Bot.event
async def on_ready():
    print("Lets go bitch")


@Bot.command()
async def prensesTiana(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Hcm 31 esports sunar')

@Bot.command()
@commands.has_role("Prenses")
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_role("Prenses")
async def clone(ctx):
    await ctx.channel.clone()

@Bot.command()
@commands.has_role("Prenses")
async def ban(ctx,member= discord.Member, *args, reason="Bilmiyorum"):
    await member.ban(reason=reason)


Bot.run(TOKEN)
