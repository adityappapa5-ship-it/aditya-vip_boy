import requests, telebot, time, random, os
from telebot import types
from flask import Flask
from threading import Thread

# --- 24/7 CLOUD ALIVE ---
app = Flask('')
@app.route('/')
def home(): return "TERMUX VIP ENGINE ACTIVE"
def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# --- CONFIG ---
API_TOKEN = '8618263406:AAHreGN69x_-g-_ZQ0VsieTWISgmxnCHBWo'
WIN_STICKER = 'CAACAgUAAxkBAAERJRhp9B-PkyNlzscUNGUAAUchyXw63g8AAisSAAJSEdhVkI_Ixu7liJU7BA'
LOSS_STICKER = 'CAACAgUAAxkBAAERJRpp9B-X_XQ3vbejkVPLEIBkdKki-QACkBQAAiMYmVWHXHRU3FIjKzsE'
API_URL = "https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json"

bot = telebot.TeleBot(API_TOKEN)

def get_data_termux_style():
    """High-Level API Bypass (Anti-Block)"""
    uas = [
        "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.036) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ]
    h = {
        'User-Agent': random.choice(uas),
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://ar-lottery01.com',
        'Referer': 'https://ar-lottery01.com/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }
    try:
        r = requests.get(API_URL, headers=h, timeout=12)
        if r.status_code == 200:
            return r.json().get('data', {}).get('list', [])
    except:
        return None

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🚀 𝗦𝗧𝗔𝗥𝗧 𝗧𝗘𝗥𝗠𝗨𝗫 𝗖𝗥𝗔𝗖𝗞 🚀"))
    bot.send_message(m.chat.id, "☠️ <b>𝕬𝕯𝕴𝕿𝖄𝕬 𝖁𝕴𝕻 𝕮𝕽𝕬𝕮𝕶</b> 💀\n\nStatus: <b>TERMUX BYPASS READY</b> ✅", parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🚀 𝗦𝗧𝗔𝗥𝗧 𝗧𝗘𝗥𝗠𝗨𝗫 𝗖𝗥𝗔𝗖𝗞 🚀")
def engine(message):
    bot.send_message(message.chat.id, "🛰️ <b>$ root@aditya:~/crack_wingo...</b>", parse_mode="HTML")
    last_p = None
    
    while True:
        try:
            history = get_data_termux_style()
            if history:
                curr_p = history[0]['issueNumber']
                
                if curr_p != last_p:
                    last_p = curr_p
                    next_p = int(curr_p) + 1
                    
                    # VIP Analysis Logic
                    last_three = [int(x['number']) for x in history[:3]]
                    avg = sum(last_three) / 3
                    pred = "🌕 𝗕𝗜𝗚" if avg >= 4.5 else "🌑 𝗦𝗠𝗔𝗟𝗟"
                    
                    # Direct Prediction Box
                    box = (
                        f"☠️ <b>𝕬𝕯𝕴𝕿𝖄𝕬 𝖁𝕴𝕻 𝕮𝕽𝕬𝕮𝕶</b> 💀\n"
                        f"━━━━━━━━━━━━━━━━━━━\n"
                        f"🔢 <b>PERIOD:</b> <code>{next_p}</code>\n"
                        f"🎯 <b>PREDICT:</b> <b>{pred}</b>\n"
                        f"🔥 <b>SIGNAL:</b> 𝕾𝕿𝕽𝕺𝕹𝕲\n"
                        f"━━━━━━━━━━━━━━━━━━━"
                    )
                    bot.send_message(message.chat.id, box, parse_mode="HTML")
                    
                    # Wait for result and send sticker
                    time.sleep(55)
                    check = get_data_termux_style()
                    if check and int(check[0]['issueNumber']) == next_p:
                        res_num = int(check[0]['number'])
                        actual = "BIG" if res_num >= 5 else "SMALL"
                        bot.send_sticker(message.chat.id, WIN_STICKER if pred.split()[1] == actual else LOSS_STICKER)
            
            time.sleep(5)
        except Exception as e:
            time.sleep(10)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()
    
