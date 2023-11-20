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
string = '1BVtsOJQBu5FlwVQJbiUOtX5VYXdG7NE1vywqE7h9BSzMupmjk6WTcV5dPbniRUBaNB_YkGVO-yOcuKuHYxyT0wXCU4t8E25V5fN_vZx6J1doLYYwZkzi0l69w4NzzFPgMS8vNdT7skebi3Z3D09hOtrkiySbWpdXNOUu8lsJN1z9cVXaiRuSvt8YoX4qPWJF-6foSUaw7U0qD1e_nO_Ru4QeG21kZPkNAP6SkGqjDKqs62EH_WRjwuPgFCTCFWgIvxSYFfDPBFOdK-yTPJ-v_Nomr0t5kobcPo7t1-RzC9uUxfPO5WayS8hfdKPPwbTj6RZZjJfujA0XHNlI9F9rA575IPVnD8E='
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
