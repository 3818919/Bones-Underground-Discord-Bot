import os
from bin import config, api
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, tasks
import socket
from urllib.request import urlopen
import pandas as pd

ServerID = config.ServerID()

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
    
    #Status Bones Underground   
    ip, port, API, timeout, retry, thumbnail = config.api()
    alert_check, alert_channel, alert = config.api_alert()
  
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
      #Server Online - API Online
      print ('Server Online')
      try:
        Players, count = api.online()
        
        #Plural Check
        if count <= 1:
          n_players = 'Player'
        else:
          n_players = 'Players'
  
        #Status Update to discord
        status = nextcord.Embed(title = 'Server Online',description = f'I have just checked and BU is online', colour = nextcord.Colour.green())
        status.add_field(name=f'**{count}** {n_players} Online', value=Players, inline=False)
        status.set_thumbnail(url=thumbnail)
        await interaction.response.send_message(embed=status, delete_after = 120)

      #Server Online API Offline
      except:
        status = nextcord.Embed(title = 'Server Online',description = f'I have just checked and BU is online', colour = nextcord.Colour.green())
        status.set_thumbnail(url=thumbnail)
        await interaction.response.send_message(embed=status, delete_after = 120)
        
        
    #Server Offline
    else:
      serverdown = nextcord.Embed(title = 'Server Offline', colour = nextcord.Colour.red())
      serverdown.add_field(name='The server is Down! OMG, we are all gonna die!', value=f"<@{alert}> Server Dying!!", inline=False)
      status.set_thumbnail(url=thumbnail)
      await interaction.response.send_message(embed=serverdown, delete_after = 120)
      return
    return  
    

def setup(bot):
  bot.add_cog(Server_Status(bot))
  print (bcolours.GREEN + 'Online Command Loaded')