import random

def ServerID():
  #Change number to your discord server ID. Bot is locked to 1 discord server.
  ID = 828442977134182401
  return ID

def api(): 
  ip = "game.bones-underground.org" #Server IP
  port = 8078 #Server Port
  API = 'https://game.bones-underground.org/api/online' #API Online List
  retry = 5 #Ping Retry
  timeout = 3 #Ping Timeout
  id = random.randint(1,500) #Generates a random npc image from BU API
  thumbnail = f'https://game.bones-underground.org/api/gfx/npcs?id={id}'
  return ip, port, API, timeout, retry, thumbnail

def api_alert():
  alert_check = False  #Set to True to activate admin alert feature.
  alert_channel = 849988039383711754  #Change number to the channel ID of the server offline alert. This will send a message to a private channel when server offline.
  alert = 512547822705311746  #Change number to server owner ID, this will @ them if server is offline.
  return alert_check, alert_channel, alert

  