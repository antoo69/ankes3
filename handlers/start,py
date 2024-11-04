from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    welcome_text = """
👋 Selamat datang di Bot Anti-GCAST!

Bot ini akan membantu Anda menjaga grup dari pesan GCAST yang mengganggu.

💵 **Harga Layanan:**
1. 1 Bulan - Rp10,000
2. 3 Bulan - Rp25,000
3. 6 Bulan - Rp45,000
4. 1 Tahun - Rp80,000

💡 **Perintah yang Tersedia:**
/bl - Tambahkan pengguna ke blacklist
/ubl - Hapus pengguna dari blacklist
/listbl - Lihat daftar pengguna yang diblacklist
/tagall - Mention semua anggota grup
/mute - Bisukan pengguna
/unmute - Aktifkan pengguna
/afk - Tandai Anda sebagai AFK
"""
    await message.reply_text(welcome_text)
