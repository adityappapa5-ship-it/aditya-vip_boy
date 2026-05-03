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

# TERE ASLI CHANNELS (DONO FIX)
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# --- 🔥 ULTRA POLYMORPHIC ENCRYPTION (VIDEO STYLE) 🔥 ---
def random_var(length=12):
    return ''.join(random.choices(string.ascii_letters, k=length))

def polymorphic_encrypt(html_content):
    # Pure code ko Byte Array (Numbers) mein badalna
    bytes_data = [ord(c) for c in html_content]
    array_str = ",".join(map(str, bytes_data))
    
    # Random variables generate karna taaki decoder confuse ho jaye
    v_data = random_var()
    v_func = random_var()
    v_output = random_var()
    v_final = random_var()
    
    header = f"\n"
    
    # Ye script runtime pe numbers ko wapas code mein badal degi
    # Isme Anti-Inspect, Anti-Debugger, aur Poly Logic sab fit hai
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        // Anti-Debugger & Inspect Lock (High Security)
        var _0xlock = function() {{ debugger; }};
        setInterval(_0xlock, 100);
        
        // Tera Data aur Magic Logic (Exactly like video 21342.mp4)
        var {v_data} = [{array_str}];
        var {v_func} = function(_0xarr) {{
            var {v_output} = "";
            for (var i = 0; i < _0xarr.length; i++) {{
                {v_output} += String.fromCharCode(_0xarr[i]);
            }}
            return {v_output};
        }};
        var {v_final} = {v_func}({v_data});
        
        document.open();
        document.write({v_final});
        document.close();
        
        // Blocking Keyboard/Mouse Shortcuts
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if (e.ctrlKey && (e.keyCode === 85 || e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 83)) return false;
            if (e.keyCode === 123) return false;
        }};
    }})();
    </script>
    <style> body {{ -webkit-user-select: none; user-select: none; pointer-events: auto; }} </style>
</head>
<body></body>
</html>"""
    return final_html

# --- 🛡️ ACCESS CHECKER (REQUEST ALLOWED) ---
def is_user_approved(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            if status == 'kicked': return False
        return True
    except: return True # Request pending hai toh skip, assume approved

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if not is_user_approved(message.from_user.id):
        bot.reply_to(message, "❌ Pehle channel join request dalo!")
        return

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        for p in [20, 50, 80, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐔𝐋𝐓𝐑𝐀 𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            # Action: Ultra Polymorphic Encryption
            final_data = polymorphic_encrypt(data)

            new_file = f"ULTRA_LOCKED_{message.document.file_name}"
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                bot.send_document(message.chat.id, f, caption="╔══════════════════════╗\n   👑 𝐔𝐋𝐓𝐑𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 𝐕𝟑\n╚══════════════════════╝\n\n👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧")
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ 𝐄𝐑𝐑𝐎𝐑: {str(e)}", message.chat.id, m.message_id)

# --- START MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]), types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 𝐂𝐇𝐄𝐂𝐊 𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋", callback_data="check"))
    
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, join request dalo aur access pao\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        bot.edit_message_text("╔══════════════════════╗\n   ✅ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃\n╚══════════════════════╝\n\nAb file bhejo, ultra lock chalu hai\.", call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == "up":
        bot.send_message(call.message.chat.id, " 📥 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐢𝐥𝐞 𝐍𝐎𝐖 📥")

bot.infinity_polling()
