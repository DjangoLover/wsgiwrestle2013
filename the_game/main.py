import os
import logging
from the_game import games as the_games
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['TEAM'] = 'X'
app.config['BOARD'] = [['X', None, None],
                       [None, 'X', None],
                       [None, None, 'X']]

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/games", defaults={'game': None})
@app.route("/games/<game>")
def games(game):
    return render_template('game_list.html', games=the_games.games)


@app.route('/tic-tac-toe', methods=['GET', 'POST'], defaults={'game':None})
@app.route('/tic-tac-toe/<game>', methods=['GET', 'POST'])
def tic_tac_toe(game):
    team = app.config['TEAM']
    team = 'X' if team == 'Y' else 'Y'
    app.config['TEAM'] = team

    if request.method == 'GET':
        if not game:
            return render_template('tic_tac_toe.html')
        else:
            return jsonify(board=app.config['BOARD'])
    else:
        if game == 'reset':
            app.config['BOARD'] = [[None, None, None],
                                   [None, None, None],
                                   [None, None, None]]
            return ''
        row = int(request.form.get('row'))
        col = int(request.form.get('col'))
        app.config['BOARD'][row][col] = team
        return jsonify(row=row,
                       col=col,
                       team=app.config['TEAM'])


def start():
    port = int(os.environ.get('PORT', 6662))
    app.run('0.0.0.0', debug=True, port=port)
