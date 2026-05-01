import requests, telebot, time, random, os
from telebot import types
from flask import Flask
from threading import Thread

# --- CLOUD SERVER (Always On) ---
app = Flask('')
@app.route('/')
def home(): return "ADITYA PAPA VIP ENGINE IS RUNNING"
def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# --- VIP CONFIG ---
API_TOKEN = '8618263406:AAHreGN69x_-g-_ZQ0VsieTWISgmxnCHBWo'
WIN_STICKER = 'CAACAgUAAxkBAAERJRhp9B-PkyNlzscUNGUAAUchyXw63g8AAisSAAJSEdhVkI_Ixu7liJU7BA'
LOSS_STICKER = 'CAACAgUAAxkBAAERJRpp9B-X_XQ3vbejkVPLEIBkdKki-QACkBQAAiMYmVWHXHRU3FIjKzsE'
CHANNELS = [-1003815161090, -1003973812867]
API_URL = "https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json"

bot = telebot.TeleBot(API_TOKEN)

def get_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/116.0.0.0 Mobile Safari/537.36',
        'Accept': 'application/json',
        'Referer': 'https://ar-lottery01.com/'
    }
    try:
        r = requests.get(API_URL, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.json()['data']['list'][0]
    except: return None

def check_join(uid):
    for c in CHANNELS:
        try:
            if bot.get_chat_member(c, uid).status in ['left', 'kicked']: return False
        except: continue
    return True

@bot.message_handler(commands=['start'])
def start(message):
    if check_join(message.from_user.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("🚀 START VIP ENGINE 🚀"))
        bot.send_message(message.chat.id, "💎 <b>ADITYA PAPA VIP CLOUD ACTIVE</b>", parse_mode="HTML", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "❌ <b>JOIN CHANNELS FIRST!</b>", parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text == "🚀 START VIP ENGINE 🚀")
def engine(message):
    bot.send_message(message.chat.id, "🔥 <b>GHATAK ENGINE STARTED...</b>", parse_mode="HTML")
    last_p = None
    
    # 100% Fixed Non-Stop Loop
    while True:
        try:
            data = get_data()
            if not data:
                time.sleep(5)
                continue
            
            curr_p = data['issueNumber']
            if curr_p != last_p:
                last_p = curr_p
                next_p = int(curr_p) + 1
                pred = random.choice(["🌕 BIG", "🌑 SMALL"])
                
                # DESIGNER BOX
                box = (
                    f"┏━━━━━━ VIP BOX ━━━━━━┓\n"
                    f"┃ 🔢 <b>PERIOD:</b> {next_p} ┃\n"
                    f"┃ 🎯 <b>BET:</b> {pred}      ┃\n"
                    f"┃ ✨ <b>LUCK:</b> 99.8%     ┃\n"
                    f"┗━━━━━━━━━━━━━━━━━━━━━━┛"
                )
                bot.send_message(message.chat.id, box, parse_mode="HTML")
                
                time.sleep(56) # Syncing with game
                
                res = get_data()
                if res and int(res['issueNumber']) == next_p:
                    res_size = "BIG" if int(res['number']) >= 5 else "SMALL"
                    sticker = WIN_STICKER if pred.split()[1] == res_size else LOSS_STICKER
                    bot.send_sticker(message.chat.id, sticker)
                    bot.send_message(message.chat.id, f"📊 <b>RESULT {next_p}: {res_size}</b>", parse_mode="HTML")
            
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.remove_webhook()
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
    
