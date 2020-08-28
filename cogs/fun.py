import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.endswith('?'):
            await message.channel.send('Yes')

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Fun(bot))
