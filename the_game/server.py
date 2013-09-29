import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

Base = declarative_base()
games = {}

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return self.id
    

class Particpation(Base):
    __tablename__ = 'participations'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    user_id = Column(String, ForeignKey('users.id'))
    team = Column(String)
    user = relationship(User, backref='my_games')
    game = relationship('Game', backref='participants')


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    winning_team = Column(String, nullable=True)
    current_turn = Column(String, ForeignKey('users.id'), nullable=True)
    game_state = Column(String)


    def __init__(self, name):
        self.name = name
        self.status = 'waiting'
        self.game_state = 'null'



def _fk_pragma_on_connect(dbapi_con, con_record):
    try:
        dbapi_con.execute('pragma foreign_keys=ON')
    except:
        pass


Session = None
session = None

def set_engine(engine):
    global Session, session
    event.listen(engine, 'connect', _fk_pragma_on_connect)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

set_engine(create_engine('sqlite:///game.sq3'))


def new_user():
    ''' Create and return a new user with a some-what random user.id '''
    count = session.query(User).count()
    user = User('Player'+str(count+1))
    session.add(user)
    session.commit()
    return user


def update_user(id, new_id):
    ''' Update user with given id to new_id '''
    user = session.query(User).filter_by(id=id).one()
    user.id = new_id
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError('User id {0} already exists'.format(new_id))


def get_user(id):
    return session.query(User).filter_by(id=id).first()


def start_game(game, user_id):
    try:
        game = games[game]()
    except KeyError:
        raise ValueError("No game {} registered.".format(game))
    session.add(game.game)
    session.commit()
    p = Particpation()
    p.user_id = user_id
    p.game_id = game.game.id
    session.add(p)
    session.commit()


def register_game(game):
    logging.warning(game)
    games[game.link] = game
    logging.warn('Games %s', games)
