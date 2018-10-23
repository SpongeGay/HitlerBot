import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Playing h!help'))
    await client.send_message(member, 'Dead To Communism Heres Nazis')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'h!germaninsult ':
        await client.send_message(message.channel,'FUCKING COMUNISM GAYS HAVE RUINED OUR BELOVED NAZI GERMANY OMG FUCK THEM WITHOUT USA THEY WAS A NEWBORN GAY SHIT BABY')
    if message.content == 'h!berlinsfear ':
        em = discord.Embed(description='')
        em.set_image(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Bundesarchiv_B_145_Bild-P054320%2C_Berlin%2C_Brandenburger_Tor_und_Pariser_Platz.jpg/280px-Bundesarchiv_B_145_Bild-P054320%2C_Berlin%2C_Brandenburger_Tor_und_Pariser_Platz.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'h!isstalingay':
        await client.send_message(message.channel,'Hes 100% Gay Communist')
    if message.content.startswith('h!ping'):
        await client.send_message(message.channel,'Nazis Ping Run <@%s> :gun:'  %(message.author.id))
    if message.content == 'h!help':
        await client.send_message(message.channel,'```This bot is beta so heres some commands: h!ping,h!berlinsfear,h!isstalingay,h!germaninsult')
client.run('NTAzMjg0MjAyMTg4NTcwNjI1.Dq-Keg.ZYYrQwLZnckne3Z6e4viAqVqMPw')
