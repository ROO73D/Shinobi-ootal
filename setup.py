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
string = '1BVtsOLEBux53eLhhDyltOQVNNkzit9ifl7fVFu_fqHPVprr-_RrUCg-946At5QY70C2uJuMkpbtB7Gj43GxY7gZmiaj4Hbob2SfUS0uKz8vxtN_BIZEGeT4f-WvPGUaF2SPQvx48OROEMnnlQZMxsospK8En2AaLyc0-GR5ccOiRCEQzsX6R7MEytOHilzB_Ex9uPjsn2SOXdWwq9jRrWx26cVfZTRCtRDxwYJcF9JaQkIj0CaD-tg3nJUyyrhnJfD--x-E4zfVqCyt0VWwE3y8XBT3-z284WBE6foMakJTui1YGmaU35D_QORnuPpw_Y-PFJj9IMTkvrOh4kvjivC2Y7TGYoy4='
client = TelegramClient(StringSession(string), api_id, api_hash)

print('Auth finished ')
@client.on(events.NewMessage(chats=[-1001982143443,-1001869117562]))
async def newMessageListener(event):
    msg = event.message
    if 'https' in msg.message:
      link = re.search(r'https:\/\/[a-zA-Z.\/1-90]+',msg.message).group(0)
      print(link)
      await client.send_message(-1001999152304,link)

with client:
    client.run_until_disconnected()
