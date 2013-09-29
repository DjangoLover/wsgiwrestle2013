from the_game import exceptions as exc

class Game:
    min_players = 0
    max_players = 0
    name = "The Game"
    link = "the-game"
    id = None
    players = None


    def add_player(self, player):
        if len(players) < max_players:
            raise exc.GameFullError("Game already has {} players!".format(
                                        len(players)))
        else:
            players.add(player)


class Player:

    def join(self, game):
        try:
            game.add_player(self)
            return True
        except exc.GameFullError:
            return False



class TicTacToe(Game):
    def __init__(self):
        self.name = 'Tic Tac Toe'
        self.link = 'tic-tac-toe'


    def __repr__(self):
        return self.name


game_list = [TicTacToe()]
games = {game.link:game for game in game_list}
