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
        'wen'
        'y '
    ]

    rps_emojis = {'r': '✊', 'p': '🖐️', 's': '✌️'}

    win = ('r', 's'), ('p', 'r'), ('s', 'p')

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

    @commands.command()
    async def rps(self, ctx, option=None):
        if not option or option.lower() not in ['rock', 'r', 'paper', 'p', 'scissors', 's']:
            embed = discord.Embed(
                title = 'Invalid choice',
                description = '''Please type one of the following options after the command:
                `rock`, `paper`, `scisscors`, `r`, `p`, `s`''',
                color = discord.Color.orange()
            )
        else:
            bot_pick = random.choice(['r', 'p', 's'])
            if option.lower()[0] == bot_pick:
                result = 'Draw!'
            elif (option.lower()[0], bot_pick) in Fun.win:
                result = 'You Win!'
            else:
                result = 'You Lose!'

            embed = discord.Embed(
                title = 'Rock, Paper, Scissors!',
                description = f'''You chose {Fun.rps_emojis[option.lower()[0]]}
                I chose {Fun.rps_emojis[bot_pick]}
                {result}''',
                color = discord.Color.orange()
            )
                    
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
