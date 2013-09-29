from the_game import server, main
from sqlalchemy import create_engine
import pytest

@pytest.fixture
def new_db():
    server.set_engine(create_engine('sqlite:///:memory:'))

@pytest.fixture
def test_client():
    main.app.config['DEBUG'] = True
    return main.app.test_client()

def test_when_new_user_is_called_user_should_exist_in_db(new_db):
    user = server.new_user()
    actual_user = server.session.query(server.User).filter_by(id=user.id).one()
    assert user.id == actual_user.id

def test_when_new_user_is_called_it_should_return_user(new_db):
    user = server.new_user()
    assert user is not None
    
def test_when_new_user_called_twice_should_return_a_different_id(new_db):
    user_one = server.new_user()
    user_two = server.new_user()
    assert user_one.id != user_two.id

def test_when_update_user_is_called_it_should_update_users_id(new_db):
    user = server.new_user()
    server.update_user(user.id, 'Bob')
    count = server.session.query(server.User).filter_by(id='Bob').count()
    assert count == 1

def test_when_update_user_is_called_it_should_not_add_a_new_user(new_db):
    user = server.new_user()
    server.update_user(user.id, 'Bob')
    count = server.session.query(server.User).count()
    assert count == 1

def test_when_update_user_is_called_if_existing_user_id_it_should_value_error(new_db):
    user_one = server.new_user()
    user_two = server.new_user()
    with pytest.raises(ValueError):
        server.update_user(user_one.id, user_two.id)

def test_when_getting_user_should_return_user_with_given_id(new_db):
    user = server.new_user()
    user_retrieved = server.get_user(user.id)
    assert user_retrieved.id == user.id

def test_when_getting_user_with_bad_id_should_return_none(new_db):
    user = server.get_user('Joker')
    assert user is None

def test_when_index_is_loaded_it_should_create_new_user(test_client, new_db):
    rv = test_client.get('/')
    assert 'Player1' in rv.data.decode()
    
def test_when_index_is_loaded_again_it_should_return_same_user(test_client, new_db):
    test_client.get('/')
    rv = test_client.get('/')
    assert 'Player1' in rv.data.decode()
    
