import nextcord
from nextcord.ext import commands
from nextcord import Embed, asset
import json 

ServerID = 192691686156140545  # FE Discord

class item_lookup(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @nextcord.slash_command(guild_ids=[ServerID], description="Checks the stats of an item in game - /item <name>")
  async def item(self, interaction: nextcord.Interaction, name):
    #Max item
    max_item = "1008"
    #Max Item
    input = name
    search = input.title()
    
    f = open("items.dat", "r")
    lines = f.readlines()
    
    outF = open("items.json", "w")
    outF.write("[")
    print('Converting Data...')
    for line in lines:
      if line.startswith("#"):
        name = line.split("#")[1]
        outF.write("{\n")
        
      if line.startswith(tuple('0123456789')):
        line = line.replace("=", ":")
        id = line.split(".")[0]
        key = line.split(".")[1]
        key = key.split(":")[0]
        value = line.split(":")[1]
        value = value.rstrip()
        p = "\""
        if key == "size":
          if id == max_item:
            outF.write(f"{p}{key}{p} : {p}{value}{p}\n" + "}" + "\n")
          else:
            outF.write(f"{p}{key}{p} : {p}{value}{p}\n" + "}," + "\n")
        else:
          #print(f"{p}{key}{p} : {p}{value}{p}{c},\n")
          outF.write(f"{p}{key}{p} : {p}{value}{p},\n")
    
    
    outF.write("]")
    outF.close()   
    
    database = "items.json"
    data = json.loads(open(database).read())
    
    item_result = nextcord.Embed(title ="Item Lookup", colour = nextcord.Colour.blue())
    
    for i in data:
      if search in i['name']:
        name = i['name']
        type = i['type']
          
        subtype = i['subtype']
        hp = i['hp']
        tp = i['tp']
        mindmg = i['mindam']
        maxdmg = i['maxdam']
        acc = i['accuracy']
        eva = i['evade']
        arm = i['armor']
        str = i['str']
        int = i['intl']
        wis = i['wis']
        agi = i['agi']
        con = i['con']
        cha = i['cha']
        scroll = i['scrollmap']
        levelreq = i['levelreq']
        classreq = i['classreq']
        strreq = i['strreq']
        intlreq = i['intlreq']
        wisreq = i['wisreq']
        agireq = i['agireq']
        conreq = i['conreq']
        chareq = i['chareq']
        spec = i['special']

        ##Define Types & Subtypes
        if type == '0':
          if spec == '3':
            item_type = 'Activated'
          else:
            item_type = 'Static Item'
            
        if type == '1':
          item_type = 'Static Item'
        if type == '2':
          item_type = 'Currency'
          
        if type == '3':
          if subtype > '0':
            item_type = 'Costume'
          else:
            if hp > 0:
              item_type = 'Consumable'
            elif tp > 0:
              item_type = 'Consumable'
            else:
              item_type = 'Static Item'
            
        if type == '4':
          item_type = 'Activated'
        if type == '9':
          item_type = 'Key'
        if type == '10':
          item_type = 'Weapon'
        if type == '11':
          item_type = 'Shield/Wings'
        if type == '12':
          item_type = 'Armor'
        if type == '13':
          item_type = 'Hat/Helmet'
        if type == '14':
          item_type = 'Boots'
        if type == '15':
          item_type = 'Gloves'
        if type == '16':
          item_type = 'Charm'
        if type == '17':
          item_type = 'Belt'
        if type == '18':
          item_type = 'Necklace'
        if type == '19':
          item_type = 'Ring'
        if type == '20':
          item_type = 'Braclet'
        if type == '21':
          item_type = 'Bracer'
        if type == '22':
          item_type = 'Booze'
        if type == '24':
          item_type = 'Hair Dye'
        if type == '25':
          item_type = 'Curse Cure'

        item_result.add_field(name="-------", value= "I found this:", inline=False)
        item_result.add_field(name="Name:", value=f"{name}", inline=False)
        item_result.add_field(name="Type:", value=item_type, inline=True)
       
        #Check for paperdoll items
        if type == '3' or type == '10' or type == '11' or type == '12' or type == '13' or type == '14' or type == '15' or type == '16' or type == '17' or type == '18' or type == '19' or type == '20' or type == '21':
          if hp > '0':
            item_result.add_field(name="HP:", value=hp, inline=True)
          if tp > '0':
            item_result.add_field(name="TP:", value=tp, inline=True)
          if mindmg > '0':
            item_result.add_field(name="Min DMG:", value=mindmg, inline=True)
          if maxdmg > '0':
            item_result.add_field(name="Max DMG:", value=maxdmg, inline=True)
          if acc > '0':
            item_result.add_field(name="Acc:", value=acc, inline=True)
          if eva > '0':
            item_result.add_field(name="Eva:", value=eva, inline=True)
          if arm > '0':
            item_result.add_field(name="Armor:", value=arm, inline=True)
          if str > '0':
            item_result.add_field(name="Str:", value=str, inline=True)
          if int > '0':
            item_result.add_field(name="Int:", value=int, inline=True)
          if wis > '0':
            item_result.add_field(name="Wis:", value=wis, inline=True)
          if agi > '0':
            item_result.add_field(name="Agi:", value=agi, inline=True)
          if con > '0':
            item_result.add_field(name="Con:", value=con, inline=True)
          if cha > '0':
            item_result.add_field(name="Cha:", value=cha, inline=True)
            
        if hp == '0' and tp == '0' and mindmg == '0' and maxdmg == '0' and acc == '0' and eva == '0' and arm == '0' and str == '0' and int == '0' and wis == '0' and agi == '0' and con == '0' and cha == '0':
          item_result.add_field(name="Result", value='No stats found', inline=True)    
        
        if levelreq > '0':
          item_result.add_field(name="Level Required:", value=levelreq, inline=True)
        if classreq > '0':
          item_result.add_field(name="Class Required:", value=classreq, inline=True)        
    
    if search in name:
      await interaction.response.send_message(embed=item_result)
      return

    

class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

def setup(bot):
  bot.add_cog(item_lookup(bot))
  print (bcolours.YELLOW + 'Item Lookup Command Loaded')