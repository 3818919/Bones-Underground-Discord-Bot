import os
from bin import config, api
import nextcord
from nextcord.ext import commands, tasks
import pandas as pd
import socket
from urllib.request import urlopen
from urllib.parse import quote
import http.client
import json
import random

try:
  from nextcord import Interaction, SlashOption
except:
  #If the bot auto updates, this will downgrade it back to being functional
  os.system("/opt/virtualenvs/python3/bin/python3 -m pip install --upgrade pip")
  os.system("pip3 install -U 'nextcord==2.0.0a10'")
  os.system('reboot')

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

TOKEN = os.environ['TOKEN']
intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(case_insensitive=True, intents=intents)
bot.remove_command('help')

#This bot stores all server chatlogs, To disable change True to False
Log_Chat = True
ServerID = config.ServerID()

Server = '''
█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀ ▄▀█ █ █▄░█ ▀█▀
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   ▄█ █▀█ █ █░▀█ ░█░

░█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀ 　 ░█─░█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █──█ █▀▀▄ █▀▀▄ 
░█▀▀▄ █──█ █──█ █▀▀ ▀▀█ 　 ░█─░█ █──█ █──█ █▀▀ █▄▄▀ █─▀█ █▄▄▀ █──█ █──█ █──█ █──█ 
░█▄▄█ ▀▀▀▀ ▀──▀ ▀▀▀ ▀▀▀ 　 ─▀▄▄▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀─▀▀ ▀▀▀▀ ▀─▀▀ ▀▀▀▀ ─▀▀▀ ▀──▀ ▀▀▀─ 

'''

print(bcolours.GREEN + Server)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
    else:
      print(bcolours.RED + f'Unable to load {filename[:-3]}')


#Checks players & server online & updates status
@tasks.loop(seconds=30)
async def status_swap(): 
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

    #If Server Online#
    if checkHost(ip, port):
      Players, count = api.online()

      status = [f'BU - {count} Players Online']
      sta = random.choice(status)
      game = nextcord.Game(sta)
      await bot.change_presence(status=nextcord.Status.online,activity=game)

    #Server Offline
    else:
      print('Server Offline')
      game = nextcord.Game(f"Nothing - Server Offline")
      await bot.change_presence(status=nextcord.Status.dnd,activity=game)
  
      if alert_check == True:
          #Sends an alert to a specified channel if the server ever goes offline. Used to alert admins.
          channel = bot.get_channel(alert_channel)
          admin = f"<{alert}>"
          message = f'{admin} **The server appears to be offline.**'
          game = nextcord.Game(f'Nothing - Server Offline')
          await channel.send(message, delete_after=57)
#End status update

#Log into discord server
@bot.event
async def on_ready():
    status_swap.start()
    print('I have logged in to the BU Discord as {0.user}'.format(bot))

#Stuff happends when a message is sent to the discord.
#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if message.author.bot:
#        return
#
#    if Log_Chat == True:
#      print(bcolours.GREEN + f'{message.author}: {message.content}')
#      channel = message.channel.name
#      path = f"chatlogs/{channel}.txt"
#      with open(path, 'a+') as f:
#          print(bcolours.GREEN + " {0.author.name}: {0.content}".format(message),
#                file=f)
#          await bot.process_commands(message)
#    else:
#      await bot.process_commands(message)

bot.run(TOKEN)