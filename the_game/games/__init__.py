import json
import logging
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
        self.game.game_state = json.dumps(self._clean_board())


    def __repr__(self):
        return self.name


    def _get_current_team(self):
        for p in self.game.participants:
            if p.user_id == self.game.current_turn:
                return p.team


    def _clean_board(self):
        return [[None, None, None],
                [None, None, None],
                [None, None, None]]
        
                
    def take_turn(self, move):
        team = self._get_current_team()
        board = json.loads(self.game.game_state)
        if board is None:
            board = self._clean_board()
        logging.warn(team)
        board[move['row']][move['col']] = team
        logging.warn(board)
        self.current_turn = self.game.participants[0].user_id
        self.game.game_state = json.dumps(board)
        server.session.add(self.game)
        server.session.commit()


    @test
    def name(self):
        return 'Tic Tac Toe'


    @test
    def link(self):
        return 'tic-tac-toe'


game_list = [TicTacToe()]
games = {game.link:game for game in game_list}

server.register_game(TicTacToe)
