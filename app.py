import os
import threading
import time
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

app = Flask(__name__)

def run_bot(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Render ko location setup
    options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
    
    try:
        driver = webdriver.Chrome(options=options)
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        driver.get(url)
        time.sleep(600)
        driver.quit()
    except:
        pass

@app.route('/')
def home():
    return '''
    <body style="font-family: Arial; text-align: center; background: #121212; color: white; padding-top: 50px;">
        <h1 style="color: #fe2c55;">🚀 TikTok Live Booster (Cloud)</h1>
        <form action="/send" method="post">
            <input type="text" name="url" placeholder="TikTok Live Link" style="width:80%; padding:15px; border-radius:10px;"><br><br>
            <input type="number" name="count" placeholder="Number of Bots" style="width:80%; padding:15px; border-radius:10px;"><br><br>
            <button type="submit" style="padding:15px 30px; background:#fe2c55; color:white; border:none; border-radius:10px;">Launch Bots 🚀</button>
        </form>
        <p style="margin-top: 20px; color: #888;">Server is 24/7 Online</p>
    </body>
    '''

@app.route('/send', methods=['POST'])
def send():
    url = request.form['url']
    count = int(request.form['count'])
    for _ in range(count):
        threading.Thread(target=run_bot, args=(url,)).start()
        time.sleep(1)
    return f"<body style='background:#121212;color:white;text-align:center;padding-top:50px;'><h2>✅ {count} Bots Sent!</h2><a href='/' style='color:#fe2c55;'>Back</a></body>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
