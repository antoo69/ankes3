from pyrogram import Client, filters
from database.blacklist import blacklist

anti_gcast_handler = Client.on_message(filters.text & filters.group)

@anti_gcast_handler
async def anti_gcast(client, message):
    if message.from_user.id in blacklist:
        await message.delete()
        await message.reply_text("Pesan ini telah dihapus karena pengguna ini ada dalam daftar blacklist.")

@Client.on_message(filters.command("bl") & filters.group)
async def blacklist_user(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        blacklist.add(user_id)
        await message.reply_text(f"Pengguna {message.reply_to_message.from_user.first_name} telah ditambahkan ke blacklist.")
    else:
        await message.reply_text("Balas pesan pengguna yang ingin ditambahkan ke blacklist.")

@Client.on_message(filters.command("unbl") & filters.group)
async def unblacklist_user(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        blacklist.discard(user_id)
        await message.reply_text(f"Pengguna {message.reply_to_message.from_user.first_name} telah dihapus dari blacklist.")
    else:
        await message.reply_text("Balas pesan pengguna yang ingin dihapus dari blacklist.")
