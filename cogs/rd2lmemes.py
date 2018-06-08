import logging
import os

import discord
from discord.ext import commands

LOGGER = logging.getLogger("red.rd2lmemes")

class RD2LMemes:
    """RD2L Memes"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def meme_image(self, ctx, filename : str):
        """Posts an image"""
        
        await self.bot.send_file(ctx.message.channel, 'data/rd2lmemes/' + filename)
        
def check_folders():
    if not os.path.exists("data/rd2lmemes"):
        print("Creating data/rd2lmemes folder...")
        os.makedirs("data/rd2lmemes")
        
def setup(bot):
    check_folders()
    cog = RD2LMemes(bot)
    bot.add_cog(cog)
