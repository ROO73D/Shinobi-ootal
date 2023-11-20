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
string = '1BVtsOJQBu7hv4E0VETwD5-zm9bWtl4q90nQWIHZ5O1TlKvlIxkxIrEh16SQK857V8Wx6UTTLtUiHSGb98kP6NtXpe5nGbg7tbB21wXKe4ARPMvRzx5yK4k7_lGvNAuZJq1lDbQcNWqlxetD7XXW6e6kmxaehoHeDN2hSYvGIPQw-JlZKyRU0kmb3RbEOTgOlxsBuE7lWJKQgC9JKDmNJF0SkBHISNAFjT0tyBMnMiDDM5y7HxMAZA4XplFaDb3zEl6UkoAw8wUawy8xGyo5I3--0xOwGzObE3H9h1vgxcQDaP0rIA4ULnO3vFIVyxjf3aAtHU4m5Rugc6VA6Qo1TpKxHfYRtubw='
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
