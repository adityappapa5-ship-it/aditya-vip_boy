import telebot
from telebot import types
import base64
import time
import os

# --- CONFIG ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# --- 🛡️ VIP REQUEST CHECKER (Fix for Pending Requests) ---
def check_vip_access(user_id):
    try:
        for channel_id in CHANNELS:
            chat_member = bot.get_chat_member(channel_id, user_id)
            # Agar status 'left' hai, tabhi access block hoga.
            # 'member', 'administrator', 'creator' aur 'restricted' ko access milega.
            if chat_member.status == 'left':
                return False
        return True
    except Exception as e:
        # Agar user ka data mil raha hai (chahe error ho), matlab usne request dali hai.
        # Sirf tab False return karega jab user bilkul unknown ho.
        return False

# --- 🔥 UI-PERFECT ENCRYPTION ---
def elite_ui_lock(html_content):
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    header = f"\n"
    
    final_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
    (function() {{
        var _0xadity = '{encoded}';
        window.onload = function() {{
            document.documentElement.innerHTML = atob(_0xadity);
            document.addEventListener('contextmenu', e => e.preventDefault());
        }};
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 100);
    }})();
    </script>
</head>
<body style="background:#000; color:#0f0; display:flex; justify-content:center; align-items:center; height:100vh;">
    <h2>👑 ADITYA VIP LOADING...</h2>
</body>
</html>"""
    return final_html

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    # 2-Second Verification Logic
    if not check_vip_access(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✨ JOIN CHANNEL 1", url=LINKS[0]))
        markup.add(types.InlineKeyboardButton("✨ JOIN CHANNEL 2", url=LINKS[1]))
        bot.reply_to(message, "❌ **ACCESS DENIED!**\n\nBhai request dalne ke baad 2 second ruko ya join karo\.", reply_markup=markup)
        return

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   🛡️ **VIP LOCKING START...**\n╚══════════════════════╝")
        
        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = elite_ui_lock(data)
            new_file = f"ULTRA_VIP_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                bot.send_document(message.chat.id, f, caption="╔══════════════════════╗\n   👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 ✅\n╚══════════════════════╝\n\n🛡️ **Design:** Safe\n👤 **Owner:** Aditya Paswan")
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, m.message_id)

# --- START MENU ---
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ JOIN CHANNEL 1", url=LINKS[0]), types.InlineKeyboardButton("✨ JOIN CHANNEL 2", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 VERIFY REQUEST", callback_data="check"))
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, join request dalo aur access pao\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if check_vip_access(call.from_user.id):
            bot.edit_message_text("✅ **Verification Success!** Ab file bhejo.", call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "❌ Request nahi mili! Pehle link pe click karke request dalo.", show_alert=True)

bot.infinity_polling()
