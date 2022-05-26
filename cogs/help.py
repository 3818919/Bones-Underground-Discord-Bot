import nextcord
from nextcord.ext import commands
from nextcord import Embed, asset

ServerID = 192691686156140545  # FE Discord

class HelpCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @nextcord.slash_command(guild_ids=[ServerID], description="Help commands for the FE Discord Bot")
  async def help(self, interaction: nextcord.Interaction):
    #Start of Main Commands List
    helpcommands = nextcord.Embed(title = 'Bot Commands', description = 'Starting Commands for the Bot', colour = nextcord.Colour.blue())
    helpcommands.add_field(name="/play", value="A shortcut to download FE.", inline=False)
    helpcommands.add_field(name="/online", value="To quickly check if the server is online of offline", inline=False)
    helpcommands.add_field(name="/staff", value="View who is working on Fallen Evolution", inline=False)
    helpcommands.add_field(name="/toplist", value="Top 100 highest level players", inline=False)
    helpcommands.add_field(name="/wiki", value="Learn more about Fallen Evolution", inline=False)
    helpcommands.add_field(name="/item <name>", value="Lookup an item info from within FE", inline=False)
    helpcommands.add_field(name="/donate", value="A qucik way to support FE", inline=False)
    #End of Main Commands List
    await interaction.response.send_message(embed=helpcommands)
    print ('Help command check')


class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

def setup(bot):
  bot.add_cog(HelpCog(bot))
  print (bcolours.YELLOW + 'Announcment Command Loaded')