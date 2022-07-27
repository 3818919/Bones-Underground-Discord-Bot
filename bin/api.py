from bin import config, api
from urllib.parse import quote
import http.client
import json
import socket
from urllib.request import urlopen
import pandas as pd

def itemlookup(name):
  name = name.title()
  if 'Of' in name:
    name = name.replace('Of', 'of')
  search = quote(name)
  try:
    conn = http.client.HTTPSConnection("game.bones-underground.org")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/items/search?name.eq={search}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
  except:
    data = "Could not find Item"
    return data

def npclookup(name):
  try:
    search = quote(name.title())
    conn = http.client.HTTPSConnection("game.bones-underground.org")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/npcs/search?name.eq={search}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
  except:
    data = "Could not find NPC"
    return data

def online():
  ip, port, API, timeout, retry, thumbnail = config.api()
  
  conn = http.client.HTTPSConnection("game.bones-underground.org")
  payload = ''
  headers = {}
  conn.request("GET", f"/api/online", payload, headers)
  res = conn.getresponse()
  data = res.read()
  data = data.decode("utf-8")
  data = pd.read_json(data)
  data.index += 1
  count = 0
  List = data.head(200) #Only show 200 Names
  #End Open API
  
  # Start of Defining Variables
  Name = List.name
  Name = sorted(Name.values)
  Players = '\n'.join(Name)
  count = len(data)
  return Players, count

def spells(name):
  try:
    search = quote(name.title())
    conn = http.client.HTTPSConnection("game.bones-underground.org")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/spells/search?name.eq={search}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
  except:
    data = "Could not find NPC"
    return data
  