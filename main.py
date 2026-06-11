import os
from google import genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("API_KEY"))

@app.route('/')
def index():
    return render_template("index.html")

app.run(port=5000)
