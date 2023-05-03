from telethon.sync import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re

api_id = 17484143
api_hash = 'b8c86dc2857d25f9b6c9af2e48739bfa'
string = '1BVtsOKQBu7UlY0bzPcLVUeE59IjM9R5Ltmsw1OvZ3yKWpLjbTl0SOeTrN35HwaiJGmYz5IZ_MfwK-MwYSB_gneQOrL8g0Zj3UQh54akrgALC5dGCTml3x4wyiTgnDSmyyD0kmHJS8hezww4nSgdjkH0JKk1WJhpl0ph77K6uPC3PM_pUYo8VdFLkiEl0yU6YeH_jxWSVV4zjYyqPR4qbQ0xNQ1akt1hAHupT4JMVx5zew-dfWbZbWr6iJut2YOduoXdgJaRzf47N9oydUbdQel7rvNHOx0Kpyt9tqy_47q2y5ZUCZmsRG38tDscPlKXbjLZTpynU2iOuw1DacmixyGs5NYTcY_4='

client = TelegramClient(StringSession(string), api_id, api_hash)

@client.on(events.NewMessage(chats=-1001803068113))
async def newMessageListener(event):
    msg = event.message
    if '/fuck' in msg.message:
      link = re.search(r'https:\/\/[a-zA-Z.\/1-90]+',msg.message).group(0)
      print(link)
      await client.send_message(-1001932519430,link)

async with client:
  asyncio.run(client.run_until_disconnected())
