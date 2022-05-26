import os
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle
import random
import pandas as pd
import socket
import asyncio
from replit import db
try:
  from nextcord import Interaction, SlashOption
except:
  os.system("/opt/virtualenvs/python3/bin/python3 -m pip install --upgrade pip")
  os.system("pip3 install -U nextcord")
  from nextcord import Interaction, SlashOption

  

class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + 

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

ServerID = 192691686156140545  # FE Discord

Server = '''

█▀▀ ▄▀█ █░░ █░░ █▀▀ █▄░█   █▀▀ █░█ █▀█ █░░ █░█ ▀█▀ █ █▀█ █▄░█
█▀░ █▀█ █▄▄ █▄▄ ██▄ █░▀█   ██▄ ▀▄▀ █▄█ █▄▄ █▄█ ░█░ █ █▄█ █░▀█

'''

print (bcolours.GREEN + Server)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
  else:
    print(bcolours.RED + f'Unable to load {filename[:-3]}')

    
#Checks players & server online & updates status
@tasks.loop(seconds=60)
async def status_swap():
  #101.98.189.250 - Ele PC
  #173.234.155.239 - VPS
  Maintinence = False
  ManualMode = False
  
  if Maintinence == False:
    ip = "101.98.189.250"
    port = 8078
    if ManualMode == True:
      port = 8077
    ele = '<@188605352223309824>'
    url = 'http://101.98.189.250/eosource.net/characters.php?ip=game.fallen-evolution.com&port=8078'

    retry = 5
    timeout = 3
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
      Players = pd.read_html(url)[0]
      Players.index += 1
      Lists = Players.head(100) #Only show 20 Items
      People = Lists.Name
      Names = People.values
      PeopleList = ', '.join(Names)
      PeopleList = PeopleList.replace(', Febot', ' ')
      PeopleList = PeopleList.replace(' Febot,', ' ')
      ponline = len(Names)
      ponline = ponline - 1
      status = f"FE - {ponline} Players Online [{PeopleList}]"
      
      if ponline == 1:
        game = nextcord.Game(status)
        await bot.change_presence(status=nextcord.Status.online, activity= game)
      
      elif ponline < 1:
        game = nextcord.Game(f'FE - Server Online')
        await bot.change_presence(status=nextcord.Status.online, activity= game)

      else:
        game = nextcord.Game(status)
        await bot.change_presence(status=nextcord.Status.online, activity= game)

    else:
      print('Server Down')
      channel = bot.get_channel(948802225713582142)
      message = f'{ele} **The server appears to be offline.**'
      name= nextcord.Game(f'Nothing - Server Offline')
      await bot.change_presence(status=nextcord.Status.dnd, activity=name)
      await channel.send(message, delete_after = 57)
      
  else:
    game = nextcord.Game('FE - Server Maintinence')
    await bot.change_presence(status=nextcord.Status.idle, activity= game)
#End status update

@bot.event
async def on_ready():
  status_swap.start()
  print('I have logged in to the FE Discord as {0.user}'.format(bot))


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.author.bot: 
    return
  
  #print (message.channel)
  print(bcolours.GREEN + f'{message.author}: {message.content}')
  channel = message.channel.name
  path = f"chatlogs/{channel}.txt" 
  with open(path, 'a+') as f:
    print("{0.author.name}: {0.content}".format(message), file=f)
    await bot.process_commands(message)


bot.run(TOKEN)