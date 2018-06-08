import logging

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
