import telebot
from telebot import types
import base64
import time
import os

# --- CONFIG ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]

# --- 🛡️ SMART REQUEST CHECKER (2-Second Verification) ---
def is_joined_or_requested(user_id):
    try:
        for channel_id in CHANNELS:
            member = bot.get_chat_member(channel_id, user_id)
            # Agar banda 'left' hai, matlab na join kiya na request daali
            if member.status == 'left':
                return False
        return True
    except Exception:
        # Agar error aata hai toh matlab banda unknown hai (No Join/No Request)
        return False

# --- 🔥 DESIGN-SAFE ENCRYPTION (NO UI CHANGE) 🔥 ---
def design_safe_lock(html_content):
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
        setInterval(function() {{ (function() {{}} .constructor("debugger")()) }}, 100);
        var _0xadity = '{encoded}';
        window.onload = function() {{
            document.documentElement.innerHTML = atob(_0xadity);
            document.addEventListener('contextmenu', e => e.preventDefault());
        }};
    }})();
    </script>
</head>
<body style="background:#000; color:#fff; display:flex; justify-content:center; align-items:center; height:100vh;">
    <div style="text-align:center;">
        <h2 style="font-family:sans-serif;">👑 ADITYA VIP LOADING...</h2>
    </div>
</body>
</html>"""
    return final_html

# --- 📥 FILE HANDLER ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    # Turant check (2 Second Logic)
    if not is_joined_or_requested(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✨ JOIN CHANNEL 1", url=LINKS[0]))
        markup.add(types.InlineKeyboardButton("✨ JOIN CHANNEL 2", url=LINKS[1]))
        bot.reply_to(message, "❌ **ACCESS DENIED!**\n\nBhai pehle dono channel join karo ya Request dalo, uske baad hi encryption hogi\.", reply_markup=markup)
        return

    if message.document.file_name.lower().endswith('.html'):
        # Uploading Animation Restore
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        for p in [25, 65, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐔𝐋𝐓𝐑𝐀-𝐋𝐎𝐂𝐊𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = design_safe_lock(data)
            new_file = f"ULTRA_VIP_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, f"rb") as f:
                bot.send_document(message.chat.id, f, caption="╔══════════════════════╗\n   👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐕𝐈𝐏 𝐋𝐎𝐂𝐊 ✅\n╚══════════════════════╝\n\n👤 **Owner:** Aditya Paswan")
            
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
    bot.send_message(message.chat.id, "╔══════════════════════╗\n      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n╚══════════════════════╝\n\nBhai, join request dalo aur 2 second mein access pao\.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        if is_joined_or_requested(call.from_user.id):
            bot.edit_message_text("✅ **Verification Done!** Ab file bhejo.", call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "❌ Aapne abhi tak Request nahi dali!", show_alert=True)

bot.infinity_polling()
                                                  
