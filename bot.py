import discord
from discord.ext import commands
from discord.utils import get
import time
from time import sleep
import json
import asyncio
import requests
import datetime
import aiohttp
#intents = discord.Intents(messages=True, members = True, guilds=True)
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)





@bot.event
async def on_ready():
    print('Online')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{members} Disocrd Mitgliedern zu'
    ))

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Bürger')
    await member.add_roles(role)
@bot.command()
async def help(ctx):
    embedVar = discord.Embed(author="Kayyz", title=f"Help", color=0x0277fd)
    embedVar.add_field(name="!help", value=f"```Zeigt die Hilfetabelle```", inline = True)
    embedVar.add_field(name="!userinfo", value=f"```User Informationen```", inline = True)
    embedVar.add_field(name="!invites", value=f"```Zeigt deine Invites an```", inline = True)
    await ctx.send(embed=embedVar)
@bot.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
            embedVar = discord.Embed(author="Kayyyz", title=f"{ctx.author} Deine Invites", color=0x0277fd)
            embedVar.add_field(name="Invites", value=f"```{totalInvites}```", inline = True)
            embedVara = discord.Embed(author="Kayyz", title=f"{ctx.author} Deine Invites", color=0x0277fd)
            embedVara.add_field(name="Invites", value=f"```0```", inline = True)
    if totalInvites <= 0:
        embedVara = discord.Embed(author="Kayyz", title=f"{ctx.author} Deine Invites", color=0x0277fd)
        embedVara.add_field(name="Invites", value=f"```0```", inline = True)
        await ctx.send(embed=embedVara)
    else:
        await ctx.send(embed=embedVar)
@bot.command()
async def userinfo(ctx, target: discord.Member):
    x = ctx.guild.members
    if not target:
        ctx.send("test")
    if target in x:
        roles = [role for role in target.roles if role != ctx.guild.default_role]
        embed = discord.Embed(title="User information", colour=0x0277fd)

        embed.set_author(name=target.name, icon_url=target.avatar_url)

        embed.set_thumbnail(url=target.avatar_url)

        embed.set_footer(text="Elements")

        fields = [("Name", str(target), False),
                ("ID", target.id, False),
                ("Status", str(target.status).title(), False),
                (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
                ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

        for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)
    else:
        await ctx.send(f'You have to ping someone from this server')
@bot.command()
async def member(ctx):
    allmember = [member.name for member in ctx.message.guild.members]
    sorted_member = sorted(allmember)
    user = member.name
    embedVar = discord.Embed(author="Kayyz", title=f"Member List,", color=0x0277fd)
    embedVar.add_field(name="Member", value=f", \n".join(sorted_member) + ".", inline = True)
    await ctx.send(embed=embedVar)
    print(member.name)
@bot.event
async def on_member_join(member):
    embedVar = discord.Embed(author="Kayyz", description=f"{member.mention} Willkommen auf Elements", color=0x0277fd)
    await bot.get_channel(1009467066090270842).send(embed=embedVar)
@bot.event
async def on_member_remove(member):
    embedVar = discord.Embed(author="Kayyz", description=f"{member.mention} hat uns verlassen.", color=0x0277fd)
    await bot.get_channel(1009472461676486756).send(embed=embedVar)



bot.run("TOKEN")
