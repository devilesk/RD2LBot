import discord
from discord.ext import commands

class ClapEmote:
    """Fuck Ryrk"""

    def __init__(self, bot):
        self.bot = bot
        self.middle_fingers = [':middle_finger: ',
                               ':middle_finger::skin-tone-1: ',
                               ':middle_finger::skin-tone-2: ',
                               ':middle_finger::skin-tone-4: ',
                               ':middle_finger::skin-tone-4: ',
                               ':middle_finger::skin-tone-5: ',
                               ]

    @commands.command(name="ryrk", pass_context=True)
    async def ryrk(self, ctx):
        """ A command for you to fuck yourself"""
        
        ret = ""
        message = ctx.message.content
        message_split = message.split(' ')[1:]
        last = 0
        for index, part in enumerate(message_split):
            ret += (self.middle_fingers[index % 6] + part + " ")
            last = index
        if not ret:
            ret = ''.join(self.middle_fingers)
        else:
            ret += self.middle_fingers[(last+1) % 6]
        await self.bot.say(ret)

    @commands.command(name="clap", pass_context=True)
    async def clap(self, ctx):
        """ A command for you to clap"""
        
        message = ctx.message.content
        upper_str_arr = map(lambda x: x.upper(), message.split(' ')[1:])
        ret = ' :clap: '.join(upper_str_arr)
        await self.bot.say(ret + " :clap:")


def setup(bot):
    bot.add_cog(ClapEmote(bot))