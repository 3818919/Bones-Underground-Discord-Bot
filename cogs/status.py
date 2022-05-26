import nextcord
from nextcord.ext import commands
import socket
import pandas as pd

ServerID = 192691686156140545  # FE Discord

class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

class Server_Status(commands.Cog, name='Server_Status'):
  def __init__(self, bot):
    self.bot = bot


  @nextcord.slash_command(guild_ids=[ServerID], description="Checks if the server is online or offline")
  async def online(self, interaction: nextcord.Interaction):
    manualmode = False
    maintain = False

    if manualmode == True:
      port = 8077
    else:
      port = 8078

    if maintain == True:
      serverdown = nextcord.Embed(title = 'Server Offline', colour = nextcord.Colour.yellow())
      serverdown.add_field(name='Server Maintinence!', value=f"The server is currently undergoing maintinence, we are aware the server is offline and will bring it back online once all work is completed.", inline=False)
      await interaction.response.send_message(embed=serverdown)
      return
      
    #Status Fallen Evolution   
    ip = "server1.fallen-evolution.com"
    retry = 5
    timeout = 3
    admins = 0
    url = 'http://101.98.189.250/eosource.net/characters.php?ip=game.fallen-evolution.com&port=8078'

    def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

    def checkHost(ip, port):
        ipup = False
        for i in range(retry):
          if isOpen(ip, port):
                        ipup = True
                        break
          else:

                        return
        return ipup

    if checkHost(ip, port):
      try:
        PlayersOnline = pd.read_html('https://fallen-evolution.com/online.php')[0]
        PlayersOnline.index += 1
        Lists = PlayersOnline.head(100) #Only show 20 Items
        People = Lists[0]
        Names = People.values
        Names = sorted(Names)
        Names.remove('Febot')
        Names.remove('Name')
        replacements = {'Saint':'**Saint**', 'Elevations':'**Elevations**','Devil':'**Devil**', 'Ghoul':'**Ghoul**'}
        replacer = replacements.get  # For faster gets.
        Names = ([replacer(n, n) for n in Names])
        PeopleList = '\n'.join(Names)
        playerson = len(Names)

        if '**Elevations**' in Names:
          admins += 1
        if '**Saint**' in Names:
          admins += 1
        if '**Devil**' in Names:
          admins +=1
        if '**Ghoul**' in Names:
          admins +=1

        playerson = playerson - admins

        #embed start
        if playerson == 1:
          if admins == 1:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Player & **{admins} Admin** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return
          else:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Player & **{admins} Admins** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return

        else:
          if admins == 1:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Players & **{admins} Admin** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return
          else:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Players & **{admins} Admins** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return
        
      
      except:
        url = 'http://www.apollo-games.com/SLN/sln.php/onlinelist?server=host:server1.fallen-evolution.com:8078'
        PlayersOnline = pd.read_html(url)[0]
        PlayersOnline.index += 1
        Lists = PlayersOnline.head(100) #Only show 20 Items
        People = Lists.Name
        Names = People.values
        Names = sorted(Names)
        Names.remove('Febot')
        replacements = {'Saint':'**Saint**', 'Elevations':'**Elevations**','Devil':'**Devil**'}
        replacer = replacements.get  # For faster gets.
        Names = ([replacer(n, n) for n in Names])
        PeopleList = '\n'.join(Names)
        playerson = len(Names)

        if '**Elevations**' in Names:
          admins += 1
        if '**Saint**' in Names:
          admins += 1
        if '**Devil**' in Names:
          admins +=1

        playerson = playerson - admins

        #embed start
        if playerson == 1:
          if admins == 1:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Player & **{admins} Admin** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return
          else:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Player & **{admins} Admins** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return

        else:
          if admins == 1:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Players & **{admins} Admin** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return
          else:
            serveron = nextcord.Embed(title = 'Server Online',description = f'I have just checked and FE is online', colour = nextcord.Colour.green())
            serveron.add_field(name=f'{playerson} Players & **{admins} Admins** Online', value=PeopleList, inline=False)
            #embed End
            await interaction.response.send_message(embed=serveron)
            return      
      
    else:
      ele_id = '<@188605352223309824>'
      serverdown = nextcord.Embed(title = 'Server Offline', colour = nextcord.Colour.red())
      serverdown.add_field(name='The server is Down! OMG, we are all gonna die!', value=f"{ele_id} HALP!!", inline=False)
      await interaction.response.send_message(embed=serverdown)
      ServerStatus = 'Offline'
      print (f'Server Check - Server {ServerStatus}')
      return
    return  
    

def setup(bot):
  bot.add_cog(Server_Status(bot))
  print (bcolours.GREEN + 'Online Command Loaded')