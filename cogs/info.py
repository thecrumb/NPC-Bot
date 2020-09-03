import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title = 'About NPC',
            description = 'NPC! Use ?help to see all the Commands'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        """Sends the invite link for this bot"""
        embed = discord.Embed(
            title = 'Invite Link',
            url = 'https://www.google.com/',
            description = 'Add NPC to another server!',
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Send a message with a question mark at the end and NPC will answer it!',
            color = discord.Color.red()
        )
        embed.add_field(
            name = 'ℹ️ Info',
            value =
'''
`about`: Gives details about the bot
`invite`: Sends the invite link for this bot
`help`: Returns this menu
`ping`: Checks the bot's response time to Discord
''',
            inline = False
        )
        embed.add_field(
            name = '🎮 Fun',
            value =
'''
`coinflip`: Flips a coin
`rps`: Rock, Paper, Scissors!
''',
            inline = False
        )
        embed.add_field(
            name = '⚙️ Config',
            value =
'''
`changeprefix`: Sets a custom command prefix for this server
''',
            inline = False
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """Checks the bot's response time to Discord"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Info(bot))
