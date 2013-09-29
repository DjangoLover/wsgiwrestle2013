import pytest
import flask
from sqlalchemy import create_engine
from the_game import main, games as the_games, server

@pytest.fixture
def test_client():
    main.app.config['DEBUG'] = True
    return main.app.test_client()


@pytest.fixture
def new_db():
    server.set_engine(create_engine('sqlite:///:memory:'))


def test_games_should_list_available_games(test_client):
    games =  {
              'game1': the_games.TicTacToe(),
              'game2': the_games.TicTacToe(),
             }
    for game in games:
        games[game].name = game
    main.the_games.games = games
     
    rv = test_client.get('/games')

    for game in games:
        assert game in rv.data.decode()
        assert games[game].name in rv.data.decode()


def test_games_some_game_start_should_start_a_new_game(test_client, new_db):
    test_client.get('/')
    rv = test_client.post('/games/tic-tac-toe/start')

    count = server.session.query(server.Game).filter_by(name='tic-tac-toe').count()

    assert count == 1


def test_games_start_should_add_current_user_to_participants(test_client, new_db):
    rv = test_client.post('/games/tic-tac-toe/start')
    game = server.session.query(server.Game).filter_by(name='tic-tac-toe').first()

    print(dir(game))
    assert game.participants[0].user_id == 'Player1'


def test_games_start_should_set_status_to_waiting_if_player_count_under_min(test_client, new_db):
    rv = test_client.post('/games/tic-tac-toe/start')
    game = server.session.query(server.Game).filter_by(name='tic-tac-toe').first()

    assert game.status == 'waiting'


def test_starting_game_that_does_not_exist_should_ValueError(test_client, new_db):
    user = server.new_user()
    with pytest.raises(ValueError):
        server.start_game('fnord', user.id)


def test_playing_a_game_should_work(test_client, new_db):
    pytest.skip()

    rv = test_client.post('/games/tic-tac-toe/start')
