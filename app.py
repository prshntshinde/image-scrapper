import logging
import os
from urllib.request import urlopen as uReq

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)