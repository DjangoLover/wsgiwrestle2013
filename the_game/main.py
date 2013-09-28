import os
import logging
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


def start():
    port = int(os.environ.get('PORT', 6662))
    app.run('0.0.0.0', debug=True, port=port)
