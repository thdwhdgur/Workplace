from flask import Flask, render_template, request
import random

print('시작중..')
app = Flask(__name__)

### ------------------- 페이지 전송 ---------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/second')
def search():
    return render_template("second.html")