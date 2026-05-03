import telebot
from telebot import types
import base64
import time
import os

# --- CONFIG ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS (Inme Bot Admin hona chahiye)
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# --- 🛡️ STRIKT JOIN CHECKER (Fixes the Bypass Problem) ---
def is_subscribed(user_id):
    try:
        for channel_id in CHANNELS:
            member = bot.get_chat_member(channel_id, user_id)
            # Agar status 'left' ya 'kicked' hai, toh access block
            if member.status in ['left', 'kicked']:
                return False
        return True
    except Exception as e:
        # Agar koi error aaye (like user not found), matlab join nahi kiya
        return False

# --- 🔥 UI-SAFE ENCRYPTION (DESIGN SECURE) 🔥 ---
def elite_encrypt(html_content):
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    header = f"\n"
    
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script>
    (function() {{
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 200);
        var _0xadity = '{encoded}';
        document.open();
        document.write(atob(_0xadity));
        document.close();
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if (e.keyCode === 123 || (e.ctrlKey && e.keyCode === 85)) return false;
        }};
    }})();
    </script>
</head>
<body></body>
</html>"""
    return final_html

# --- 📥 FILE HANDLER (WITH LOCK) ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    # Sabse pehle check ki banda join hai ya nahi
    if not is_subscribed(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
        markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
        bot.reply_to(message, "❌ **ACCESS DENIED!**\n\nBhai pehle dono channels join karo, uske baad hi file encrypt hogi.", reply_markup=markup)
        return

    # Agar join hai toh encryption chalu
    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "⚙️ **Processing VIP Lock...**")
        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = elite_encrypt(data)
            new_file = f"ADITYA_VIP_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                bot.send_document(message.chat.id, f, caption="╔══════════════════════╗\n   👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 ✅\n╚══════════════════════╝\n\n👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧")
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, m.message_id)

# --- START MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 𝐕𝐄𝐑𝐈𝐅𝐘 𝐉𝐎𝐈𝐍", callback_data="check"))
    
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, bina join kiye bot kaam nahi karega\. Pehle join karo\!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if is_subscribed(call.from_user.id):
            bot.edit_message_text("✅ **Verification Success!**\n\nAb aap HTML file bhej sakte ho, main usey encrypt kar dunga.", call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "❌ Aapne abhi tak join nahi kiya!", show_alert=True)

bot.infinity_polling()
