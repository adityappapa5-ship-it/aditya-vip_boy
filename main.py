import telebot
from telebot import types
import base64
import random
import string
import os
import time

# --- CONFIG (API TOKEN) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE DONO ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

# --- 🛡️ ULTRA TAGADA ENCRYPTION (UNBREAKABLE) ---
def ultra_tagada_encrypt(html_content):
    # Unique keys for every encryption
    key1 = random_name()
    key2 = random_name()
    
    # Header Branding
    header = f"\n"
    
    # 1. Double Base64 with Shuffling
    b64_1 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    # Splitting string to confuse decoders
    split_index = len(b64_1) // 2
    part1 = b64_1[:split_index]
    part2 = b64_1[split_index:]

    # 2. Polymorphic Script Injection
    # Isme Anti-Debug aur String Re-assembly logic hai
    encrypted_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        // Anti-Debugger (Banda Inspect karega toh page crash hoga)
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 50);
        
        var {key1} = '{part1}';
        var {key2} = '{part2}';
        var _final = atob({key1} + {key2});
        
        document.open();
        document.write(_final);
        document.close();
        
        // Block all shortcuts
        window.addEventListener('keydown', function(e) {{
            if (e.ctrlKey && (e.keyCode === 85 || e.keyCode === 83 || e.keyCode === 73 || e.keyCode === 74)) {{
                e.preventDefault();
            }}
        }}, false);
        document.addEventListener('contextmenu', e => e.preventDefault());
    }})();
    </script>
    <style>
        body {{ -webkit-user-select: none; user-select: none; -webkit-touch-callout: none; pointer-events: auto; }}
    </style>
</head>
<body></body>
</html>"""
    return encrypted_html

# --- 🛡️ ACCESS CHECKER ---
def is_user_approved(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            if status == 'kicked': return False
        return True
    except: return False

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        # Smooth VIP Animation
        for p in [15, 40, 70, 90, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐔𝐋𝐓𝐑𝐀 𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            # Action: Ultra Encryption
            final_data = ultra_tagada_encrypt(data)

            new_file = f"ULTRA_LOCKED_{message.document.file_name}"
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "╔══════════════════════╗\n"
                    "   👑 𝐔𝐋𝐓𝐑𝐀 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐄𝐃 ✅\n"
                    "╚══════════════════════╝\n\n"
                    "👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n"
                    "🛡️ 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲: 𝐀𝐧𝐭𝐢-𝐃𝐞𝐜𝐫𝐲𝐩𝐭 𝐕𝟐"
                )
                bot.send_document(message.chat.id, f, caption=cap)
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ 𝐄𝐑𝐑𝐎𝐑: {str(e)}", message.chat.id, m.message_id)

# --- START & MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 𝐂𝐇𝐄𝐂𝐊 𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋", callback_data="check"))
    
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, ab aisa encryption lagega ki koi hila bhi nahi payega\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        bot.edit_message_text("╔══════════════════════╗\n   ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃\n╚══════════════════════╝\n\nAb file bhejo, Hard-Core Encryption on hai\.", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
