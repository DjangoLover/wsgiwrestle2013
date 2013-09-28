from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return self.id
    

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

