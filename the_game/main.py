import os
import logging
from the_game import server, games as the_games
from flask import Flask, make_response, render_template, request, jsonify,\
                  render_template

app = Flask(__name__)
app.config['TEAM'] = 'X'
app.config['BOARD'] = [['X', None, None],
                       [None, 'X', None],
                       [None, None, 'X']]

def current_user():
    '''Get and return the current user from their cookie.'''
    user_id = request.cookies.get('user_id')
    user = server.get_user(user_id)
    if user is None:
        user = server.new_user()
    return user


@app.route("/")
def main():
    user = current_user()
    resp =  make_response(render_template('index.html', user = user))
    resp.set_cookie('user_id', user.id)
    return resp


@app.route("/games", defaults={'game': None})
@app.route("/games/<game>")
def games(game):
    return render_template('game_list.html', games=the_games.games)


@app.route("/games/<game>/start", methods=['GET', 'POST'])
def start_game(game):
    server.start_game(game, current_user().id)
    return jsonify(thing=game)


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
