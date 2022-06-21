import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 342212467046350849:
        client.load_extension(f'cogs.{extension}')
        print(f'Класс {extension} был загружен\n')

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 342212467046350849:
        client.unload_extension(f'cogs.{extension}')
        print(f'Класс {extension} был выгружен\n')

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 342212467046350849:
        client.reload_extension(f'cogs.{extension}')
        print(f'Класс {extension} был перезапущен\n')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('token')