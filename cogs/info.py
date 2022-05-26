import nextcord
from nextcord.ext import commands
from nextcord import Embed, asset
import io
import aiohttp
import numpy as np
import pandas as pd

ServerID = 192691686156140545  # FE Discord

class infoCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @nextcord.slash_command(guild_ids=[ServerID], description="Lists the top FE Players (By Level)")
  async def toplist(self, interaction: nextcord.Interaction):
    topplayers = pd.read_html('https://fallen-evolution.com/topplayers.php')[0]
    topplayers.index += 1
    Lists = topplayers.head(50)
    Players = Lists[0]
    Level = Lists[1]
    Players = Players.values
    Level = Level.values
    Players = np.delete(Players, 0)
    Players = Players.tolist()
    
    for i in range(len(Players)):
      Players[i] = Players[i].capitalize() 
      
    Level = np.delete(Level, 0)
    Players = '\n'.join(Players)
    Levels = '\n'.join(Level) 
    TopList = nextcord.Embed(title = 'Top 50 Players',url = 'https://fallen-evolution.com/topplayers', colour = nextcord.Colour.blue())
    TopList.add_field(name="Name", value=Players, inline=True)
    TopList.add_field(name="Level", value=Levels, inline=True)
    TopList.set_footer(text='Powered by Fallen Evolution |  www.fallen-evolution.com/topplayers')
    await interaction.response.send_message(embed=TopList, delete_after = 120)  


  @nextcord.slash_command(guild_ids=[ServerID], description="Find out more about Fallen Evolution")
  async def wiki(self, interaction: nextcord.Interaction):
    link = 'https://wiki.fallen-evolution.com/index.php/Main_Page'
    logo = 'https://wiki.fallen-evolution.com/resources/assets/logo.png' 
    wiki=nextcord.Embed(title="FE Wiki", url=link, description="For information about Fallen Evolution, visit the wiki.")
    wiki.set_thumbnail(url=logo)
    await interaction.response.send_message(embed=wiki) 


class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

def setup(bot):
  bot.add_cog(infoCog(bot))
  print (bcolours.GREEN + 'Toplist Command Loaded\nTopdonations Command Loaded\nWiki Command Loaded')