from datetime import datetime

from discord import Embed, TextChannel
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="embed", description="Sending Embed")
    async def test(self, ctx: SlashContext, title: str, description: str, color: str, channel: TextChannel = None):
        if not channel:
            channel = ctx.channel

        embed = Embed(title=title, description=description, colour=int(color.replace('#', ''), 16),
                      timestamp=datetime.now())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await channel.send(embed=embed)
        msg = await ctx.send(
            embed=Embed(description='Embed has been successfully sent to the <#{}> channel!'.format(channel.id)))
        await msg.delete(delay=10)
