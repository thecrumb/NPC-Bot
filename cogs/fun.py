import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    idk = [
        'who',
        'what',
        'when',
        'where',
        'why',
        'how',
        'wat',
        'wot',
        'wut',
        'y '
    ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.endswith('?'):
            if (' or ' in message.content.lower() or
                    any(message.content.lower().startswith(starter) for starter in Fun.idk)):
                await message.channel.send("I don't know")
                return
            await message.channel.send(random.choice(['Yes', 'No']))

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(random.choice(['Heads!', 'Tails!']))

def setup(bot):
    bot.add_cog(Fun(bot))
