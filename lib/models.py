import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///db/movies.db', echo=True)

association_table = Table(
    'movie_actor_association',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))
    salary = Column(Integer)
    character_name = Column(String)

    movie = relationship("Movie", backref=backref("roles", cascade="all, delete-orphan"))
    actor = relationship("Actor", backref=backref("roles", cascade="all, delete-orphan"))

    def __repr__(self):
        return f'Role: {self.character_name} - {self.movie.title}'
    
    def actor(self):
        return self.actor

    def movie(self):
        return self.movie

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    movies = relationship("Movie", secondary=association_table, back_populates="actors")

    def __repr__(self):
        return f'Actor: {self.name}'
    
    def roles(self):
        return self.roles

    def movies(self):
        return [role.movie for role in self.roles]

    def total_salary(self):
        return sum(role.salary for role in self.roles)

    def blockbusters(self):
        return [role.movie for role in self.roles if role.movie.box_office_earnings > 50000000]

    @classmethod
    def most_successful(cls):
        session = Session()
        actors = session.query(cls).all()
        highest_salary_actor = max(actors, key=lambda actor: actor.total_salary())
        session.close()
        return highest_salary_actor
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    box_office_earnings = Column(Integer())

    actors = relationship("Actor", secondary=association_table, back_populates="movies")

    def __repr__(self):
        return f'Movie: {self.title}'
    
    def roles(self):
        return self.roles

    def actors(self):
        return [role.actor for role in self.roles]

    def cast_role(self, actor, character_name, salary):
        role = Role(actor=actor, character_name=character_name, salary=salary)
        self.roles.append(role)

    def all_credits(self):
        return [f'{role.character_name}: Played by {role.actor.name}' for role in self.roles]

    def fire_actor(self, actor):
        role = next((r for r in self.roles if r.actor == actor), None)
        if role:
            self.roles.remove(role)

    def total_salary(self):
        return sum(role.salary for role in self.roles)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

