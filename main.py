import telebot
from telebot import types
import random
import string
import os
import time

# --- CONFIG (API TOKEN CONNECTED) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE DONO CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# Faltu ka kachra code generate karne ke liye (Size badhane ke liye)
def get_massive_junk(count=200):
    junk = ""
    for i in range(count):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=80))
        junk += f"var _0xaditya_junk_{i} = '{random_str}';\n        "
    return junk

# --- 🔥 ULTRA MEGA-SIZE ENCRYPTION (PHOTO & VIDEO STYLE) 🔥 ---
def ultra_mega_encrypt(html_content):
    # Pure code ko Byte-Array (Numbers) mein badalna
    byte_array = [ord(c) for c in html_content]
    
    header = f"\n"
    
    # Isme hum massive garbage daal rahe hain taaki file badi ho jaye
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        // --- 🗑️ GARBAGE LAYER (FILE SIZE INCREASER) ---
        {get_massive_junk()}
        
        // --- 🛡️ ANTI-DEBUGGER LOCK ---
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 100);
        
        // --- 📊 BYTE MAPPING (NUMBERS STYLE) ---
        var _0xdata = [{",".join(map(str, byte_array))}];
        
        var _0xexec = "";
        for (var i = 0; i < _0xdata.length; i++) {{
            _0xexec += String.fromCharCode(_0xdata[i]);
        }}
        
        document.open();
        document.write(_0xexec);
        document.close();
        
        // --- 🚫 FULL SYSTEM LOCK (UNCOPYABLE) ---
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.addEventListener('selectstart', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey) || (e.ctrlKey && e.keyCode === 85)) return false;
        }};
    }})();
    </script>
    <style> body {{ -webkit-user-select: none; user-select: none; pointer-events: auto; }} </style>
</head>
<body></body>
</html>"""
    return final_html

# --- 🛡️ AUTO-VERIFY LOGIC (REQUEST ALLOWED) ---
def has_access(user_id):
    try:
        # Bot admin hai toh wo status check kar lega
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            # Agar banda kicked hai sirf tabhi block karo
            if status == 'kicked': return False
        return True
    except:
        return True # Request pending hai toh bhi access mil jayega

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if not has_access(message.from_user.id):
        bot.reply_to(message, "❌ Pehle channel join request dalo!")
        return

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        for p in [30, 65, 90, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐌𝐄𝐆𝐀-𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = ultra_mega_encrypt(data)
            new_file = f"MEGA_LOCKED_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = "╔══════════════════════╗\n   👑 𝐌𝐄𝐆𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 ✅\n╚══════════════════════╝\n\n👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n🛡️ 𝐒𝐢𝐳𝐞: 𝐌𝐚𝐱𝐢𝐦𝐮𝐦"
                bot.send_document(message.chat.id, f, caption=cap)
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ 𝐄𝐑𝐑𝐎𝐑: {str(e)}", message.chat.id, m.message_id)

# --- START MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 𝐂𝐇𝐄𝐂𝐊 𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋", callback_data="check"))
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, join request dalo aur system automatic access de dega\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        bot.edit_message_text("╔══════════════════════╗\n   ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃\n╚══════════════════════╝\n\nAb file bhejo, Mega-Encryption on hai\.", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
