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

# --- 🛡️ STRICT MEMBERSHIP CHECK (Bypass Fix) ---
def is_subscribed(user_id):
    try:
        for channel_id in CHANNELS:
            member = bot.get_chat_member(channel_id, user_id)
            if member.status in ['left', 'kicked']:
                return False
        return True
    except:
        return False

# --- 🔥 ULTIMATE UI-SAFE ENCRYPTION (NO DESIGN CHANGE) 🔥 ---
def final_ui_safe_encrypt(html_content):
    # Pure code ko Base64 mein convert karna (Emojis aur CSS ke liye safe)
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    header = f"\n"
    
    # Isme 'document.write' hata diya hai taaki UI glitch na kare
    final_html = f"""{header}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <script>
    (function() {{
        // Anti-Debugger Lock
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 100);

        var _0xdata = '{encoded}';
        var _0xdecoded = atob(_0xdata);

        // Rendering logic jo design nahi bigadti
        window.onload = function() {{
            document.documentElement.innerHTML = _0xdecoded;
            
            // Full Security Lock after loading
            document.addEventListener('contextmenu', e => e.preventDefault());
            document.addEventListener('selectstart', e => e.preventDefault());
        }};

        document.onkeydown = function(e) {{
            if (e.keyCode === 123 || (e.ctrlKey && e.keyCode === 85)) return false;
        }};
    }})();
    </script>
</head>
<body style="background:#000; color:#fff; display:flex; justify-content:center; align-items:center; height:100vh; font-family:sans-serif;">
    <div id="loader">👑 ADITYA VIP LOADING...</div>
</body>
</html>"""
    return final_html

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if not is_subscribed(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
        markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
        bot.reply_to(message, "❌ **Bhai pehle dono channel join karo!**", reply_markup=markup)
        return

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "💎 **𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐍𝐆 𝐖𝐈𝐓𝐇 𝐔𝐈-𝐒𝐀𝐅𝐄 𝐌𝐎𝐃𝐄...**")
        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = final_ui_safe_encrypt(data)
            new_file = f"VIP_FIXED_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                bot.send_document(message.chat.id, f, caption="╔══════════════════════╗\n   👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 ✅\n╚══════════════════════╝\n\n🛡️ **Design:** 100% Original\n👤 **Owner:** Aditya Paswan")
            
            bot.delete_message(message.chat.id, m.message_id)
            os.remove(new_file)
        except Exception as e:
            bot.edit_message_text(f"❌ Error: {str(e)}", message.chat.id, m.message_id)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐", url=LINKS[1]))
    markup.add(types.InlineKeyboardButton("🔄 𝐕𝐄𝐑𝐈𝐅𝐘 𝐉𝐎𝐈𝐍", callback_data="check"))
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, join lock fixed hai\. Ab bina join kiye encrypt nahi hoga\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if is_subscribed(call.from_user.id):
            bot.edit_message_text("✅ **Verification Done!** Ab file bhejo.", call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "❌ Join nahi kiya abhi tak!", show_alert=True)

bot.infinity_polling()
