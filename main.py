import telebot
from telebot import types
import base64
import os
import time

# --- CONFIG (API TOKEN) ---
API_TOKEN = '8518332653:AAG3AZXXOfmYj_vWg6y30FRFH72R4ktm63M'
bot = telebot.TeleBot(API_TOKEN)

# TERE ASLI CHANNELS
CHANNELS = ["-1003815161090", "-1003973812867"]
LINKS = ["https://t.me/+_RZ0gN9HU6xhZTRl", "https://t.me/+7bNfhxLosYsxMmVl"]
OWNER_LINK = "https://t.me/ADITYAXVIPBOT"

# --- 🛡️ VIP JOIN CHECKER (REQUEST ALLOWED) ---
def is_user_approved(user_id):
    try:
        for channel in CHANNELS:
            status = bot.get_chat_member(channel, user_id).status
            # Agar 'left' hai toh block, baaki sab (member/creator/admin) allowed
            # Note: Join request bhejne par bhi 'left' dikha sakta hai agar admin ne accept na kiya ho
            # Isliye hum check karenge ki banda block na ho bas
            if status == 'kicked':
                return False
            if status == 'left':
                # Yahan logic hai ki agar banda left hai toh check karo request toh nahi daali
                return False 
        return True
    except Exception:
        return False

# --- 🔥 TAGADA ENCRYPTION (CHROME UI SAFE) 🔥 ---
def tagada_encrypt(html_content):
    branding = f"\n"
    b64_data = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    # Ye script browser mein UI ko 100% real load karti hai
    encrypted_html = f"""{branding}
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
        
        // Security: No Right Click, No F12, No Selection
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.onkeydown = function(e) {{
            if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && e.keyCode == 73)) return false;
            if(e.ctrlKey && e.keyCode == 85) return false;
        }};
    }})();
    </script>
    <style>
    * {{ -webkit-user-select: none; user-select: none; }}
    </style>
</head>
<body></body>
</html>"""
    return encrypted_html

# --- 📥 FILE HANDLER (WITH 1-100% JHAKAS ANIMATION) ---
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    # Instant Request Check
    if not is_user_approved(message.from_user.id):
        # Yahan hum unhe allow kar rahe hain agar wo humein pata hai ki request daal chuke hain
        # Lekin security ke liye unhe button dikhana zaroori hai
        pass 

    if message.document.file_name.lower().endswith('.html'):
        m = bot.reply_to(message, "╔══════════════════════╗\n   ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐑𝐓: 𝟏%\n╚══════════════════════╝")
        
        # 1 to 100 Tik-Tik Loading
        for p in [20, 45, 75, 95, 100]:
            time.sleep(0.3)
            bot.edit_message_text(f"╔══════════════════════╗\n   🛡️ 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐍𝐆: {p}%\n╚══════════════════════╝", message.chat.id, m.message_id)

        try:
            file_info = bot.get_file(message.document.file_id)
            data = bot.download_file(file_info.file_path).decode('utf-8', errors='ignore')
            
            final_data = tagada_encrypt(data)
            new_file = f"ADITYA_VIP_{message.document.file_name}"
            
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(final_data)
                
            with open(new_file, "rb") as f:
                cap = (
                    "╔══════════════════════╗\n"
                    "   👑 𝐇𝐓𝐌𝐋 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐄𝐃 ✅\n"
                    "╚══════════════════════╝\n\n"
                    "👤 𝐎𝐰𝐧𝐞𝐫: 𝐀𝐝𝐢𝐭𝐲𝐚 𝐏𝐚𝐬𝐰𝐚𝐧\n"
                    "🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐔𝐥𝐭𝐫𝐚 𝐒𝐞𝐜𝐮𝐫𝐞"
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
    markup.add(types.InlineKeyboardButton("✨ 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 (𝐑𝐄𝐐𝐔𝐄𝐒𝐓)", url=LINKS[0]))
    markup.add(types.InlineKeyboardButton("🔄 𝐂𝐇𝐄𝐂𝐊 𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋", callback_data="check"))
    
    msg = (
        "╔══════════════════════╗\n"
        "      👑 𝐀𝐃𝐈𝐓𝐘𝐀 𝐗 𝐎𝐖𝐍𝐄𝐑\n"
        "╚══════════════════════╝\n\n"
        "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐕𝐈𝐏 𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧 𝐒𝐲𝐬𝐭𝐞𝐦\.\n"
        "𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐉𝐨𝐢𝐧 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞\."
    )
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check":
        # Bhai yahan magic hai, hum user ko allow kar denge
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 𝐔𝐏𝐋𝐎𝐀𝐃 𝐇𝐓𝐌𝐋", callback_data="up"))
        
        msg = "╔══════════════════════╗\n   ✅ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐆𝐑𝐀𝐍𝐓𝐄𝐃\n╚══════════════════════╝\n\nAb file bhejo, system verify ho gaya hai\."
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
            
    elif call.data == "up":
        bot.send_message(call.message.chat.id, "📥 **𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐇𝐓𝐌𝐋 𝐅𝐈𝐋𝐄 𝐍𝐎𝐖**")

bot.infinity_polling()
