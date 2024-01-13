#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "28361260"
API_HASH = "38c131498b9cdeacde8f1f763d466840"
BOT_TOKEN = "6866261943:AAGEmTcS1SxGSluma3zDCociVIx7FowfT3g"
SESSION = "BQGwwiwAmLSA3NIT4wZCvCREsPVjl56KO7iSeVyjKBU4jr-oYtUtIJiK6fRHxAoVtD4veHuXhoMxZOTEXHRfAYl_5L-QR3DNFNL9T0_udHIPe9OuKpX_DuOJcu3QDXTUoHroM3-YLcs10xRVM5H9w1S85PL1izy-HDyvEDNI_rv8fa8RE7NqQCgGZdg1lL0JKtKUIgF68kJEpvWdXIct1qUi-ALAamlZ73XeNMHnuzqPBYfW8yOufCSyfDh-AiCevAn7Tfpq38BNFDLTIJ3J_XL_6j5boOWsuWzRvDNezMSPbR286AanXwAns8BO9B5YHHWMD2Dzztc8o6lIGBfyz3Io4HhrjgAAAAFzrmw3AA"
FORCESUB = "log_akshsy"
AUTH = "6235778103"
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
