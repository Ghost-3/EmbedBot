from discord.ext import commands
from discord_slash import SlashCommand

from cfg import TOKEN, PREFIX
from events import Events
from commands import Commands


bot = commands.Bot(command_prefix=PREFIX)
slash = SlashCommand(bot, sync_commands=True)
bot.add_cog(Commands(bot))
bot.add_cog(Events(bot))
bot.run(TOKEN)
