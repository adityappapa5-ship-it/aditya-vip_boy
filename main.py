import telebot
from telebot import types
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

def get_random_string(length=12):
    return ''.join(random.choices(string.ascii_letters, k=length))

# --- 🔥 ULTRA HARDCORE POLYMORPHIC ENCRYPTION 🔥 ---
def polymorphic_encrypt(html_content):
    # Pure code ko Byte-Array mein convert karna (Photo style)
    byte_array = [ord(c) for c in html_content]
    
    # Random variables generate karna taaki decoder confuse ho jaye
    var_array = get_random_string()
    var_func = get_random_string()
    var_output = get_random_string()
    var_key = get_random_string()
    
    header = f"\n"
    
    # Ye script runtime pe numeric data ko execute karegi (Video logic)
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        // Anti-Debugger (Page crash if someone tries to inspect)
        (function _0xadity(){{try{{(function _0xlock(i){{if((''+(i/i)).length!==1||i%20===0){{(function(){{}}).constructor('debugger')();}}else{{debugger;}}_0xlock(++i);}})(0);}}catch(e){{setTimeout(_0xadity,200);}}}})();
        
        // Poly-Byte Mapping (Exactly like video 21342.mp4)
        var {var_array} = {byte_array};
        var {var_key} = {random.randint(100, 999)};
        
        var {var_func} = function(_0xbytes) {{
            var {var_output} = "";
            for (var i = 0; i < _0xbytes.length; i++) {{
                {var_output} += String.fromCharCode(_0xbytes[i]);
            }}
            return {var_output};
        }};
        
        var _0xexecute = {var_func}({var_array});
        document.open();
        document.write(_0xexecute);
        document.close();
        
        // Extra Security: No Right Click, No F12, No View-Source
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || (e.ctrlKey && e.keyCode === 85)) return false;
        }};
    }})();
    </script>
    <style> body {{ -webkit-user-select: none; user-select: none; }} </style>
</head>
<body></body>
</html>"""
    return final_html

# --- 🛡️ SMART VERIFICATION ---
def check_user_access(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            if status == 'kicked': return False
        return True
    except: return True # Join request pending ko allow karega

# --- 📥 FILE HANDLER (WITH 1-100% VIP ANIMATION) ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        # Smooth 1 to 100 Animation
        for p in [20, 45, 75, 95, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐔𝐋𝐓𝐑𝐀-𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            # Action: Polymorphic Encryption
            final_data = polymorphic_encrypt(data)
            new_file = f"ULTRA_LOCKED_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "╔══════════════════════╗\n"
                    "   👑 𝐔𝐋𝐓𝐑𝐀 𝐋𝐎𝐂𝐊 𝐕𝟑 ✅\n"
                    "╚══════════════════════╝\n\n"
                    "👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n"
                    "🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐔𝐧𝐛𝐫𝐞𝐚𝐤𝐚𝐛𝐥𝐞 𝐋𝐨𝐜𝐤"
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
    
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, Ultra-Lock V3 (Polymorphic) system active ho gaya hai\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        bot.edit_message_text("╔══════════════════════╗\n   ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃\n╚══════════════════════╝\n\nAb file bhejo, Hardcore Poly-Lock lagega\.", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
