import os
import logging
from the_game import games as the_games
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/games", defaults={'game': None})
@app.route("/games/<game>")
def games(game):
    return render_template('game_list.html', games=the_games.games)


def start():
    port = int(os.environ.get('PORT', 6662))
    app.run('0.0.0.0', debug=True, port=port)
