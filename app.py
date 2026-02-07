import os
import threading
import time
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

app = Flask(__name__)

def run_bot(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Render ko path milaune
    options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
    
    driver = webdriver.Chrome(options=options)
    # Stealth settings...
    driver.get(url)
    time.sleep(600)
    driver.quit()

@app.route('/')
def home():
    return '<h1>Bot Panel Online</h1>' # Agi ko HTML yaha halnu hola

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
