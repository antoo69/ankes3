from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

tagall_in_progress = False

tagall_handler = Client.on_message(filters.command("tagall") & filters.group)

@tagall_handler
async def tagall(client, message: Message):
    global tagall_in_progress
    if tagall_in_progress:
        await message.reply_text("Tagall sedang berlangsung. Gunakan /stop_tagall untuk menghentikannya.")
        return
    
    tagall_in_progress = True
    await message.reply_text("Memulai tagall... Gunakan /stop_tagall untuk membatalkan.")
    
    mentions = []
    async for member in client.get_chat_members(message.chat.id):
        if not tagall_in_progress:
            await message.reply_text("Tagall dihentikan.")
            break
        
        user_mention = f"@{member.user.username}" if member.user.username else f"[{member.user.first_name}](tg://user?id={member.user.id})"
        mentions.append(user_mention)
        
        if len(" ".join(mentions)) > 3500:
            await message.reply_text(" ".join(mentions))
            mentions = []
            await asyncio.sleep(1)

    if mentions and tagall_in_progress:
        await message.reply_text(" ".join(mentions))
    
    if tagall_in_progress:
        await message.reply_text("Tagall selesai.")
    tagall_in_progress = False

@Client.on_message(filters.command("stop_tagall") & filters.group)
async def stop_tagall(client, message: Message):
    global tagall_in_progress
    if tagall_in_progress:
        tagall_in_progress = False
        await message.reply_text("Proses tagall telah dihentikan.")
    else:
        await message.reply_text("Tidak ada tagall yang sedang berlangsung.")
