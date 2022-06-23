
import discord
import random
import requests
from discord.ext import commands
from discord.commands import (  # Импортирует декоратор для слэш комманд
    slash_command,
)



class Slash(commands.Cog): 
    
    def __init__(self, client):
        self.client = client

    #@slash_command()
    #async def info(self, ctx):
    #   await ctx.respond("Hi, this is a global slash command from a cog!")


    
    @slash_command(name = 'avatar', description = 'ворует аватарку пользователя на сервере')
    async def getavatar(self, ctx, member: discord.Member = None):
        show_avatar = discord.Embed(

        color = discord.Color.dark_red()
            )
        show_avatar.set_image(url='{}'.format(member.avatar))
        await ctx.respond(embed=show_avatar)
    
    @slash_command(name = 'info', description = 'показывает информацию о пользователе')
    async def getinfo(self, ctx, member: discord.Member = None):
        date_format = "%d/%m/%Y, %H:%M"
        embed = discord.Embed(color = 0xdfa3ff, description=member.mention)
        embed.set_author(name=str(member), icon_url=member.avatar)
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Joined", value=member.joined_at.strftime(date_format))
        embed.add_field(name="Registered", value=member.created_at.strftime(date_format))
        await ctx.respond(embed=embed)

    
def setup(client):
    client.add_cog(Slash(client))