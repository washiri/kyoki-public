import discord
from discord.ext import commands

class Events(commands.Cog): 
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣧⠻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠟⢻⣿⣿⣿⡿⢿⣷⣌⡛⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⢿⡿⠃⣰⣿⣿⣿⣿⣿⣄⠢⣍⡛⢌⠻⣿
⣿⣿⣿⣿⣿⡇⠻⣿⣿⣿⣿⣿⣿⣷⡌⢡⣾⡿⠭⠝⣛⠻⠿⢿⣷⣌⡻⣷⡄⡹
⣿⣿⡇⢻⣿⣷⢸⣦⣙⠻⢿⣿⣿⠟⣠⡀⢡⣼⣿⣿⣦⣬⣷⣦⣤⣍⣛⠜⣿⡜
⣿⣿⢣⣆⠻⣿⡌⢿⣿⣿⣶⣬⣁⣐⡻⠿⠄⠙⠿⠿⢟⣛⣛⣛⣋⣭⣍⢩⣤⣝
⣿⡏⡼⢏⣀⠹⣿⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢸⣿⣿
⣿⢱⣴⣿⣿⣷⣌⡻⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⣻⣿⢸⣿⣿
⡿⣸⣿⣿⣿⣿⣿⠿⠷⢦⣼⣿⣿⣿⣿⣿⣿⣿⣋⠖⢁⣤⣶⣿⣿⣿⣿⢸⣿⣿
⡇⠿⠟⣋⣭⠭⣵⣾⣿⣶⡶⠾⠭⠙⢿⣿⣿⣿⣿⣾⣿⣿⣿⡟⡿⣿⢿⢸⣿⣿
⢡⣶⣿⣿⣿⣾⣿⣿⣿⡟⢘⣋⣍⣝⠊⣿⣿⣿⣿⣿⣿⣿⣿⣼⣶⣃⣾⠸⣿⣿
⣿⣿⢈⣿⣿⠃⢸⣿⣿⢣⠋⠶⠶⢊⢹⡿⠿⠛⠛⠉⠻⣿⣿⣿⣿⣿⡿⠇⣿⣿
⣿⡇⢾⣿⣿⢠⣿⣿⣿⣎⠻⠿⠛⢣⠃⠄⣠⣴⣶⣶⡆⣿⣿⣿⡿⠋⠄⠄⢻⣿
⢛⣓⠸⢟⣛⠘⣩⣶⣶⡌⡼⠋⣿⡸⡰⣾⣿⣿⣿⡿⢃⣿⠿⠋⣀⣀⠄⣠⡜⣿
⠈⠙⠂⠛⠿⠃⣩⣴⣶⣶⣦⣴⣿⣷⣱⣮⠭⠭⢔⣒⣩⡴⢚⣨⡜⣡⣾⣿⣷⠹ 
                                      ''') 
    
    # edit handler
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author == self.client.user:
            return
        channel = self.client.get_channel(874660675442593812)
        guild = self.client.get_guild(724014966008447066)
        embed = discord.Embed(title=f"{guild.name}", description=f"**{before.author.mention} изменил сообщение в канале {before.channel.mention}**\n\n**Старое:**\n ```\n{before.content}\n```\n**Новое:**\n```\n{after.content}\n```", color=0x40cc88,)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text='test')
        await channel.send(embed=embed)
        return

    # delete handler
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.client.user: 
            return
        channel = self.client.get_channel(874660675442593812)
        guild = self.client.get_guild(724014966008447066)
        embed = discord.Embed(title=f"{guild.name}", description=f"**{message.author.mention} удалил сообщение в канале {message.channel.mention}**\n\n```{message.content}\n```", color=0x40cc88,)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text='Создатель отсталый')
        if message.attachments:
            embed = discord.Embed(title=f"{guild.name}", description=f"**{message.author.mention} удалил сообщение в канале {message.channel.mention}**\n\n**{message.content}**\n", color=0x40cc88,)
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text='Создатель отсталый')
            embed.set_image(url=message.attachments[0].url)
        await channel.send(embed=embed)




def setup(client):
    client.add_cog(Events(client))

