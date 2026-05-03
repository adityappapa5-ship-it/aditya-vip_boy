import telebot
from telebot import types
import base64
import os
import time

# --- CONFIG (API TOKEN CONNECTED) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]
OWNER_LINK = "https://t.me/ADITYAXVIPBOT"

# --- 🛡️ SMART JOIN CHECKER (REQUESTS APPROVED) ---
def is_user_approved(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            # Agar banda left hai toh block, baaki sab cases (member/request) mein allow
            if status == 'left':
                return False
        return True
    except Exception:
        return False

# --- 🔥 ULTRA TAGADA ENCRYPTION (NO UI CHANGE) 🔥 ---
def tagada_encrypt(html_content):
    # Branding inside code
    header = f"\n"
    b64_data = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    # Ye script design ko safe rakhti hai aur code lock karti hai
    encrypted_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        var _0xadity = '{b64_data}';
        document.open();
        document.write(atob(_0xadity));
        document.close();
        
        // Anti-Copy & Anti-Inspect Security
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74 || e.keyCode == 67))) return false;
            if(e.ctrlKey && e.keyCode == 85) return false;
        }};
    }})();
    </script>
    <style>
    * {{ -webkit-user-select: none; user-select: none; -webkit-touch-callout: none; }}
    </style>
</head>
<body></body>
</html>"""
    return encrypted_html

# --- 📥 FILE HANDLER (WITH 1-100% VIP ANIMATION) ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if not is_user_approved(message.from_user.id):
        bot.reply_to(message, "╔══════════════════════╗\n   ❌ 𝐉𝐎𝐈𝐍 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐏𝐄𝐍𝐃𝐈𝐍𝐆\n╚══════════════════════╝\n\nBhai pehle channel join request dalo!")
        return

    if message.document.file_name.lower().endswith('.html'):
        # VIP PROCESSING EFFECT
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        # Smooth Tik-Tik Increment
        for p in [15, 35, 60, 85, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = tagada_encrypt(data)
            new_file = f"VIP_ENCRYPTED_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "╔══════════════════════╗\n"
                    "   👑 𝐇𝐓𝐌𝐋 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐄𝐃 ✅\n"
                    "╚══════════════════════╝\n\n"
                    "👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n"
                    "🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐔𝐥𝐭𝐫𝐚 𝐒𝐞𝐜𝐮𝐫𝐞\n\n"
                    "🎯 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: " + LINKS[0]
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
    
    msg = (
        "╔══════════════════════╗\n"
        "      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n"
        "╚══════════════════════╝\n\n"
        "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐕𝐈𝐏 𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧 𝐒𝐲𝐬𝐭𝐞𝐦\.\n"
        "𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐨𝐫 𝐒𝐞𝐧𝐝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞\."
    )
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if is_user_approved(call.from_user.id):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
            markup.add(types.InlineKeyboardButton("👨‍💻 𝐎𝐖𝐍𝐄𝐑", url=OWNER_LINK))
            
            msg = (
                "╔══════════════════════╗\n"
                "    👑 𝐕𝐈𝐏 𝐌𝐄𝐍𝐔 𝐀𝐂𝐓𝐈𝐕𝐄\n"
                "╚══════════════════════╝\n\n"
                "𝐀𝐜𝐜𝐞𝐬𝐬 𝐆𝐫𝐚𝐧𝐭𝐞𝐝\. 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 𝐍𝐨𝐰\."
            )
            bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
        else:
            bot.answer_callback_query(call.id, "❌ Pehle dono channels join request dalo!", show_alert=True)
            
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
            
