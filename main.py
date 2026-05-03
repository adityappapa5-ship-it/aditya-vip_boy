import telebot
from telebot import types
import base64
import os
import time

# --- CONFIG (NEW TOKEN CONNECTED) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]
OWNER_LINK = "https://t.me/ADITYAXVIPBOT"

# --- 🛡️ FORCE JOIN CHECKER ---
def is_user_joined(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            if status == 'left':
                return False
        return True
    except:
        return False

# --- 🔥 ULTRA TAGADA ENCRYPTION (REAL UI PRESERVED) 🔥 ---
def tagada_encrypt(html_content):
    # #ADITYA_ENCRYPT_BOT branding inside code
    branding = f"\n"
    
    # Pure HTML ko Base64 mein badalna taaki Logic aur UI safe rahe
    b64_data = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    # Ye script bina Design/Logic bigade code ko browser mein inject karegi
    encrypted_html = f"""{branding}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    /* #ADITYA_ENCRYPT_BOT SECURITY */
    (function() {{
        var _0xadity = '{b64_data}';
        document.open();
        document.write(atob(_0xadity));
        document.close();
        
        // Anti-Selection & Anti-Right-Click
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74 || e.keyCode == 67))) return false;
            if(e.ctrlKey && e.keyCode == 85) return false;
        }};
    }})();
    </script>
    <style>
    /* Disables text selection without affecting UI layout */
    * {{ -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }}
    </style>
</head>
<body>
</body>
</html>"""
    return encrypted_html

# --- 📥 FILE HANDLER (ENCRYPT ONLY) ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if not is_user_joined(message.from_user.id):
        bot.reply_to(message, "❌ **Pehle dono channels join karo!**")
        return

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "┌──────────────────────┐\n   🔐 ENCRYPTING: 1%\n└──────────────────────┘")
        
        # 1 to 100 Animation
        for p in [30, 60, 90, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"┌──────────────────────┐\n   🔐 ENCRYPTING: {p}%\n└──────────────────────┘", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            # 100% Logic aur UI safe encryption
            final_data = tagada_encrypt(data)

            new_file = f"ENCRYPTED_BY_ADITYA_{message.document.file_name}"
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "┌──────────────────────┐\n"
                    "   👑 HTML ENCRYPTION DONE ✅\n"
                    "└──────────────────────┘\n\n"
                    "🛡️ Security: High Layer\n"
                    "👤 Owner: Aditya Paswan\n\n"
                    "🎯 Channel: " + LINKS[0]
                )
                bot.send_document(message.chat.id, f, caption=cap)
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ ERROR: {str(e)}", message.chat.id, m.message_id)

# --- START & MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎯 JOIN CHANNEL 1", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("🎯 JOIN CHANNEL 2", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 CHECK APPROVAL", callback_data="check"))
    
    msg = (
        "┌──────────────────────┐\n"
        "      👑 ADITYA X OWNER\n"
        "└──────────────────────┘\n\n"
        "Bhai, ye bot HTML ko encrypt karega bina uska UI bigade.\n\n"
        "⚠️ **Pehle upar diye gaye dono channels join karein!**"
    )
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if is_user_joined(call.from_user.id):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("📤 UPLOAD HTML", callback_data="up"))
            markup.add(types.InlineKeyboardButton("👨‍💻 OWNER", url=OWNER_LINK))
            
            msg = (
                "┌──────────────────────┐\n"
                "   👑 VIP ENCRYPTOR ON\n"
                "└──────────────────────┘\n\n"
                "Ab apni HTML file bhejo, design 100% safe rahega."
            )
            bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
        else:
            bot.answer_callback_query(call.id, "❌ Pehle dono channels join karo!", show_alert=True)
            
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "🔮 **SEND YOUR HTML FILE TO ENCRYPT**")

bot.infinity_polling()
