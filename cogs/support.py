import nextcord
from nextcord.ext import commands
import urllib3
from bs4 import BeautifulSoup

ServerID = 192691686156140545  # FE Discord

class Share_Cog(commands.Cog, name='Share Cog'):

  def __init__(self, bot):
    self.bot = bot


  @nextcord.slash_command(guild_ids=[ServerID], description="Check who is working on Fallen Evolution")
  async def staff(self, interaction: nextcord.Interaction):
    staff = ['Elevations | HGM','Devil | HGM','Saint | HGM']
    staff =  '\n'.join(staff)
    stafflist = nextcord.Embed(title = 'FE Staff', description = staff, colour = nextcord.Colour.purple())
    await interaction.response.send_message(embed=stafflist)
    

  @nextcord.slash_command(guild_ids=[ServerID], description="A shorcut to quickly download Fallen Evolution")
  async def play(self, interaction: nextcord.Interaction):
    http = urllib3.PoolManager()
    my_url = 'https://fallen-evolution.com/FEC.php'
    response = http.request('GET', my_url)
    sopa = BeautifulSoup(response.data, features="html5lib")
    current_link = ''
    for link in sopa.find_all('a'):
      current_link = link.get('href')
      if current_link.endswith('.msi/file'):
        download = current_link 
        logo = 'https://wiki.fallen-evolution.com/resources/assets/logo.png' 
        Play=nextcord.Embed(title="Play FE Today!", url=download, description="Click the link to download the client.", color=0xfac400)
        Play.set_thumbnail(url=logo)
        await interaction.response.send_message(embed=Play)
        
  
  @nextcord.slash_command(guild_ids=[ServerID], description="A shorcut to quickly donate to Fallen Evolution")
  async def donate(self, interaction: nextcord.Interaction):
    #Patreon Link
    donate=nextcord.Embed(title="Support Fallen Evolution", url="https://fallen-evolution.com/donate", description="Donating helps the server in every way", color=0xfac400)
    donate.set_thumbnail(url="https://wiki.fallen-evolution.com/resources/assets/logo.png")
    donate.set_footer(text="You help us pay for the server, website, advertising, ddos protection & more.")
    #End of Patreon Link
    await interaction.response.send_message(embed=donate)
    
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

def setup(bot):
  bot.add_cog(Share_Cog(bot))
  print (bcolours.GREEN + 'Play Command Loaded\nStaff Command Loaded')