from the_game import exceptions as exc
from the_game import server

class Player:

    def join(self, game):
        try:
            game.add_player(self)
            return True
        except exc.GameFullError:
            return False


def test(foo):
    return 'tic-tac-toe'

class TicTacToe:
    def __init__(self):
        self.game = server.Game('tic-tac-toe')


    def __repr__(self):
        return self.name


    @test
    def name(self):
        return 'Tic Tac Toe'


    @test
    def link(self):
        return 'tic-tac-toe'


game_list = [TicTacToe()]
games = {game.link:game for game in game_list}

server.register_game(TicTacToe)
