import os
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB = os.getenv("MONGO_DB")
OWNER_ID = int(os.getenv("OWNER_ID"))

app = Client(
    "anti_gcast_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
