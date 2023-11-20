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
string = '1BVtsOJQBu5xOSsWKxfSkBijy6Rqu6jz58FWJNGPUlhgoJvruaIYNU6VGeP5d9RKxbVQ6PIkCZXhixzB3RNREyafx51t1-l0r_mxoBOWM7lx-m1R0oGePGcFP7JnRabTHsHSQrSs1N0dYMVU782WDY3TMMRMtzGSWfIPKq4mwgtMftLZ_xzEdb8WhebTDuhednJRnhB13HHrkUvtbLNCEr8c0f-mM-w-wZJW9k79ZBsKcX-Ewm5LiybqWarQQHVOi0Ra5MEi3fGor29WkGmu16o4qLYFuAbuoHhZwy3bVoGbnYkZyZp0054gKhz2j2bX-IXbQ03LDi4MjiGgFBq12NMugJ_pw9Lg='

client = TelegramClient(StringSession(string), api_id, api_hash)

print('Auth finished ')
@client.on(events.NewMessage(chats=[-1001982143443,-1001768742734,-1001869117562]))
async def newMessageListener(event):
    msg = event.message
    if 'https' in msg.message:
      link = re.search(r'https:\/\/[a-zA-Z.\/1-90]+',msg.message).group(0)
      print(link)
      await client.send_message(-1001999152304,link)

with client:
    client.run_until_disconnected()
