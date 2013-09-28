import os
import logging
from the_game import server
from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    user_id = request.cookies.get('user_id')
    user = server.get_user(user_id)
    if user is None:
        user = server.new_user()
    resp =  make_response(render_template('index.html', user = user))
    resp.set_cookie('user_id', user.id)
    return resp

def start():
    port = int(os.environ.get('PORT', 6662))
    app.run('0.0.0.0', debug=True, port=port)
