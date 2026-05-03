import telebot
from telebot import types
import random
import os
import time

# --- CONFIG (API TOKEN) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# --- 🔥 TAGADA BYTE-ARRAY ENCRYPTION LOGIC 🔥 ---
def hardcore_encrypt(html_content):
    # Pure code ko numeric array mein badalna (Jo tune 21339.jpg mein dekha)
    byte_array = [ord(c) for c in html_content]
    
    # Array ko strings mein todna taaki aur mushkil ho jaye
    array_str = ",".join(map(str, byte_array))
    
    header = f"\n"
    
    # Ye script runtime pe numbers ko wapas code mein badal degi
    # Isme Anti-Inspect aur Anti-Debugger pehle se fit hai
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        // Anti-Inspect & Debugger (Lock System)
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 200);
        
        // Tera Numeric Data (Byte Mapping)
        var _0xadityData = [{array_str}];
        
        var _0xrender = _0xadityData.map(function(c) {{
            return String.fromCharCode(c);
        }}).join('');
        
        document.open();
        document.write(_0xrender);
        document.close();
        
        // Full Security Lock
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if (e.ctrlKey && (e.keyCode === 85 || e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 83)) return false;
            if (e.keyCode === 123) return false;
        }};
    }})();
    </script>
    <style>
        body {{ -webkit-user-select: none; user-select: none; pointer-events: auto; }}
    </style>
</head>
<body></body>
</html>"""
    return final_html

# --- 🛡️ ACCESS CHECKER (REQUEST ALLOWED FIX) ---
def is_user_approved(user_id):
    try:
        # Hum sirf block status check karenge taaki request wale bando ko dikkat na ho
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            if status == 'kicked': return False
        return True
    except: return True # Request pending hai toh bhi access de do

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        for p in [20, 55, 85, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐁𝐘𝐓𝐄-𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            # Action: Hardcore Byte Array Encryption
            final_data = hardcore_encrypt(data)

            new_file = f"BYTE_LOCKED_{message.document.file_name}"
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "╔══════════════════════╗\n"
                    "   👑 𝐁𝐘𝐓𝐄-𝐀𝐑𝐑𝐀𝐘 𝐋𝐎𝐂𝐊 ✅\n"
                    "╚══════════════════════╝\n\n"
                    "👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n"
                    "🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐔𝐧𝐛𝐫𝐞𝐚𝐤𝐚𝐛𝐥𝐞"
                )
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
    
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, Byte-Array encryption active ho gaya hai\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        bot.edit_message_text("╔══════════════════════╗\n   ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐑𝐄𝐀𝐃𝐘\n╚══════════════════════╝\n\nAb file bhejo, Hardcore lock lagega\.", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
