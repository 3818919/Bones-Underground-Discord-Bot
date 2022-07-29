from bin import api, config
import nextcord
from nextcord.ext import commands

ServerID = config.DServ()

class infoCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  #Item Lookup
  @nextcord.slash_command(guild_ids=[ServerID], description="Lookup in game items & stats.")
  async def item(self, interaction: nextcord.Interaction, name):
    data = api.itemlookup(name)
    try:
      for i in data:
        item_id = i['id']
        name = i['name']
        type = i['type']
        spec = i['special']
        try:
          hp = i['hp']
          tp = i['tp']
          mindmg = i['min_damage']
          maxdmg = i['max_damage']
          aoe = i['aoe_range']
          acc = i['accuracy']
          eva = i['evade']
          arm = i['armor']
          str = i['str']
          int = i['int']
          wis = i['wis']
          agi = i['agi']
          con = i['con']
          cha = i['cha']
          levelreq = i['level_req']
          classreq = i['class_req']
          strreq = i['str_req']
          intlreq = i['int_req']
          wisreq = i['wis_req']
          agireq = i['agi_req']
          conreq = i['con_req']
          chareq = i['cha_req']
        except:
          pass
  
      thumbnail = api.itempic(item_id)
      item = nextcord.Embed(title = 'Item Lookup',description = f'Looks like I was able to find something, take a look:', colour = nextcord.Colour.green())
      item.set_thumbnail(url=thumbnail)
  
      try:
        item.add_field(name='Name', value=name, inline=True)
        item.add_field(name='Type', value=type, inline=True)
        item.add_field(name='Rarity', value=spec, inline=True)
        if hp > 0:
          item.add_field(name='HP', value=hp, inline=True)
        if tp > 0:
          item.add_field(name='TP', value=tp, inline=True)
        if levelreq == 0:
          item.add_field(name='LVL Req', value='None', inline=True)
        else:
          item.add_field(name='LVL Req', value=levelreq, inline=True)
        item.add_field(name='⚔️Min DMG', value=mindmg, inline=True)
        item.add_field(name='⚔️Max DMG', value=maxdmg, inline=True)
        if aoe == 0:
          item.add_field(name='AOE Range', value=f'None', inline=True)
        else:
          item.add_field(name='AOE Range', value=f'{aoe} Squares', inline=True)
        item.add_field(name='🎯Acc', value=acc, inline=True)
        item.add_field(name='👟Evade', value=eva, inline=True)
        item.add_field(name='🛡️Armor', value=arm, inline=True)
        item.add_field(name='💪STR', value=str, inline=True)
        item.add_field(name='🧠INT', value=int, inline=True)
        item.add_field(name='📚WIS', value=wis, inline=True)
        item.add_field(name='🚶AGI', value=agi, inline=True)
        item.add_field(name='❤️CON', value=con, inline=True)
        item.add_field(name='✨CHA', value=cha, inline=True)
        if classreq:
          item.add_field(name='Class Requirement', value=classreq, inline=True)
        if strreq:
          item.add_field(name='STR Requirement', value=strreq, inline=True)
        if intlreq:
          item.add_field(name='INT Requirement', value=intlreq, inline=True)
        if wisreq:
          item.add_field(name='WIS Requirement', value=wisreq, inline=True)
        if agireq:
          item.add_field(name='AGI Requirement', value=agireq, inline=True)
        if conreq:
          item.add_field(name='CON Requirement', value=conreq, inline=True)
        if chareq:
          item.add_field(name='CHA Requirement', value=chareq, inline=True)
      except:
        pass
        
      await interaction.response.send_message(embed=item, delete_after = 120)
      
    except:
      error = "Sorry, I wasn't able to find that item."
      await interaction.response.send_message(error, delete_after = 120)


  #NPC Lookup
  @nextcord.slash_command(guild_ids=[ServerID], description="Lookup in game items & stats.")
  async def npc(self, interaction: nextcord.Interaction, name):
    data = api.npclookup(name)
    try:
      for i in data:
        try:
          npc_id = i['id']
          name = i['name']
          type = i['type']
          boss = i['boss']
          if boss == 0:
            boss = False
          else:
            boss = True
          hp = i['hp']
          mindmg = i['min_damage']
          maxdmg = i['max_damage']
          acc = i['accuracy']
          eva = i['evade']
          arm = i['armor']
          exp = i['experience']
          drops = i['drops']
          for i in drops:
            itemname = []
            itemname.append(i['name'])
          loc = i['locations']
          for i in loc:
            locname = []
            locname.append(i)
            
        except:
          if 'Could not find' in data:
            error = data
            await interaction.response.send_message(error, delete_after = 120)
            return
          pass
  
      thumbnail = api.npcpic(npc_id)
      item = nextcord.Embed(title = 'NPC Lookup',description = f'Looks like I was able to find something, take a look:', colour = nextcord.Colour.green())
      item.set_thumbnail(url=thumbnail)
      
      try:
        item.add_field(name='Name', value=name, inline=True)
        item.add_field(name='Type', value=type, inline=True)
        item.add_field(name='HP', value=hp, inline=True)
        item.add_field(name='⚔️Min DMG', value=mindmg, inline=True)
        item.add_field(name='⚔️Max DMG', value=maxdmg, inline=True)
        item.add_field(name='🎯Acc', value=acc, inline=True)
        item.add_field(name='👟Evade', value=eva, inline=True)
        item.add_field(name='🛡️Armor', value=arm, inline=True)
        item.add_field(name='EXP', value=exp, inline=True)
        item.add_field(name='Drops', value=itemname, inline=True)
        item.add_field(name='Locations', value=locname, inline=True)
        
      except:
        pass
        
      await interaction.response.send_message(embed=item, delete_after = 120)
    except:
      error = 'Sorry, I could not find the npc you are looking for.'
      await interaction.response.send_message(error, delete_after = 30)

  #Spells Lookup
  @nextcord.slash_command(guild_ids=[ServerID], description="Lookup in game items & stats.")
  async def spell(self, interaction: nextcord.Interaction, name):
    data = api.spells(name)
    try:
      for i in data:
        try:
          spell_id = i['id']
          name = i['name']
          cast_time = i['cast_time']
          hp = i['hp']
          mindmg = i['min_damage']
          maxdmg = i['max_damage']
          acc = i['accuracy']
          target = i['target_type']
          cost = i['tp_cost']
          learn = i['taught_by']
          for t in learn:
            teacher = t['name']
           
        except:
          if 'Could not find' in data:
            error = data
            await interaction.response.send_message(error, delete_after = 120)
            return
          pass
  
      thumbnail = api.spellpic(spell_id)
      item = nextcord.Embed(title = 'NPC Lookup',description = f'Looks like I was able to find something, take a look:', colour = nextcord.Colour.green())
      item.set_thumbnail(url=thumbnail)
      
      try:
        item.add_field(name='Name', value=name, inline=True)
        item.add_field(name='Targeting', value=target, inline=True)
        if hp != 0:
          item.add_field(name='HP', value=hp, inline=True)
        item.add_field(name='Min DMG', value=mindmg, inline=True)
        item.add_field(name='Max DMG', value=maxdmg, inline=True)
        item.add_field(name='Acc', value=acc, inline=True)
        item.add_field(name='Cast Time', value=f'{cast_time}s', inline=True)
        item.add_field(name='Mana Cost', value=cost, inline=True)
        item.add_field(name='Learn From', value=teacher, inline=True)
        
      except:
        pass
        
      await interaction.response.send_message(embed=item, delete_after = 120)
    except:
      error = 'Sorry, I could not find the npc you are looking for.'
      await interaction.response.send_message(error, delete_after = 30)

class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
# bcolors.RED + print (bcolours.GREEN + CREATOR)

def setup(bot):
  bot.add_cog(infoCog(bot))
  print (bcolours.GREEN + 'Item Lookup Command Loaded')