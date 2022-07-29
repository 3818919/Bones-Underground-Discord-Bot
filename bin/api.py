from bin import config
from urllib.parse import quote
import http.client
import json
import pandas as pd
import random


def itemlookup(name):
  domain = config.API()
  name = name.title()
  if 'Of' in name:
    name = name.replace('Of', 'of')
  search = quote(name)
  try:
    conn = http.client.HTTPSConnection(domain)
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
    domain = config.API()
    search = quote(name.title())
    conn = http.client.HTTPSConnection(domain)
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
  domain = config.API()
  conn = http.client.HTTPSConnection(domain)
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
  Players = Players.replace("Cirras", "**Cirras**")
  count = len(data)
  return Players, count

def spells(name):
  try:
    domain = config.API()
    search = quote(name.title())
    conn = http.client.HTTPSConnection(domain)
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

def thumbnail():
  domain = config.API()
  num = random.randint(1,500)
  thumbnail = f"https://{domain}/api/gfx/npcs?id={num}"
  return thumbnail

def itempic(itemid):
  domain = config.API()
  itempic = f"https://{domain}/api/gfx/items?id={itemid}"
  return itempic

def npcpic(npcid):
  domain = config.API()
  npcpic = f"https://{domain}/api/gfx/npcs?id={npcid}"
  return npcpic

def spellpic(spellid):
  domain = config.API()
  spellpic = f"https://{domain}/api/gfx/spells?id={spellid}"
  return spellpic