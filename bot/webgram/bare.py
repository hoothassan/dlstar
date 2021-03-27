import telethon
from telethon import errors, functions, types, events , helpers
import asyncio
import aiohttp
import urllib.parse
from . import (
    Config, StreamTools
)
import io
import re
import os.path
import requests
from contextlib import redirect_stdout
from subprocess import PIPE, STDOUT, Popen
from telethon.tl.types import InputFile
from telethon.sessions import StringSession
from telethon.tl.types import (
    UserStatusOnline,
    UserStatusOffline,
)

 
class BareServer(Config, StreamTools):
    client: telethon.TelegramClient
    
    def __init__(self, loop: asyncio.AbstractEventLoop):
        
        self.client = telethon.TelegramClient(
            StringSession(), #self.config.SESS_NAME,
            self.config.APP_ID,
            self.config.API_HASH,
            loop=loop
        ).start(bot_token=self.config.BOT_TOKEN)
        

        @self.client.on(events.NewMessage)
        async def download(event : events.NewMessage.Event):
            if event.is_private :
                #await self.set(event.sender_id , "dlgram")
                try:
                    await event.client(functions.channels.GetParticipantRequest(channel=self.config.channel,user_id=event.sender_id))
                except errors.UserNotParticipantError:
                    await event.reply(f"First join to our official channel to access the bot or get the newest news about the bot\n\n@{self.config.channel}\n\nAfter that /start the bot aging.")
                    return
                if event.file :
                    sender = await event.get_sender()
                    msg = await event.client.send_file(self.config.STATS_CHANNEL, file=event.message.media, caption=f"@{sender.username}|[{event.sender_id}](tg://user?id={event.sender_id})/{event.message.id}")
                    #url = f"{msg.chat_id}/{msg.id}/{urllib.parse.quote(self.get_file_name(event))}"
                    hash = self.encode(f"{msg.id}")
                    url = f"{hash}/{urllib.parse.quote(self.get_file_name(event))}"
                    await event.reply(f"Link to download file: \n\n📥 : {self.config.ROOT_URI}/w/{url}")
                    return
                elif urls := self.Find(event.raw_text) :
                    await event.reply("Link to File \n not available...")

                await event.reply("Send an image or any file to get a link to download it...")

 
        