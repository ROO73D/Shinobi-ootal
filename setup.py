# from telethon.sync import TelegramClient
# from telethon import TelegramClient, events
# from telethon.sessions import StringSession
# import re

# api_id = 17484143
# api_hash = 'b8c86dc2857d25f9b6c9af2e48739bfa'
# string = '1BVtsOL8Bu1MYDQ0iWTrfOLyqhGp93Q8PUaykOJwYfd01H69cyYVl7ULlBEqplFH3sFHxR3cB3VCOJA8mmXOXN-_hjXtHlpzzVPE7W93Rex0Hkt5SsFbcdez8NIPorhw2y3VjIAVFFTrt3l1iqm4rccaphLuC8i60OT8hvXHpfQPJ3cVckVkRLJvtT_0qM8NaG_BQzsACMrj3hg-WFPpjqBf9lLE4KkqV8SsdQqsLKow0gH0Dd8KZdVOT746h_TNFzcCWq6nHg1tU8ZS5xi8B8WHzhSlJM_s1DLjOITKHTkw_fUjAQjo6Kvf7tkCM1QoYcc1gjTm2DXI05YLMVvzPKZmDLTZxXp8='

# client = TelegramClient(StringSession(string), api_id, api_hash)

# print('Auth finished ')
# @client.on(events.NewMessage(chats=-1001803068113))
# async def newMessageListener(event):
#     msg = event.message
#     if '/fuck' in msg.message:
#       link = re.search(r'https:\/\/[a-zA-Z.\/1-90]+',msg.message).group(0)
#       print(link)
#       await client.send_message(-1001932519430,link)

# with client:
#   client.run_until_disconnected()

from telethon.sync import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re

api_id = 17484143
api_hash = 'b8c86dc2857d25f9b6c9af2e48739bfa'
string = '1BVtsOJoBu3X4YeOMIoD8_CE1sELBCNAgwWnr-vBxXONqQ8-4sr9pnvLH8ENOJdPiO8RqXXEiJ0E-WmPNNBWZUu3VTq3P_7FYbHFsDiwpuY-hPEDKKFz0GwSZ4WvCfz7nVPenG9fUCoLxUeOJcIa7Aq86qw6g43inye1nqtymYprHRoLjuKFoQSUiLr8KRGw7IdNc5TBNjDtyQt5vF-BcHrYmbScfOGggD3FHByNzn5NtsvpaNqzcAsz2qhLgk4YJaF-6UvCfcepC1M3wn4ewfvJgvBuFAeGhH-D7XkdKu1a1PxQbSk7gIEeJ3Dw-0apG2ljz--J3oc2DuKeWxem0QLa3vQzts4g='
client = TelegramClient(StringSession(string), api_id, api_hash)

print('Auth finished ')
@client.on(events.NewMessage(chats=[-1001983705786,-1002033680699,-1001768742734,-1001982143443,-1001869117562,-1001665768915,-1001501537847,-1001568323849,-1002107400730]))
async def newMessageListener(event):
    movie = event.message.text
    if 'http' in movie:
      urls = re.findall('https:\/\/[a-zA-Z1-90\.]+\/?[a-zA-Z1-90\.]+\/?[a-zA-Z1-90]+', movie)
      for i in urls:
        print(i)
        await client.send_message(-1001999152304,i)
          
with client:
    client.run_until_disconnected()
