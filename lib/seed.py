from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Actor, Movie, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/movies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Role).delete()
    session.query(Movie).delete()
    session.query(Actor).delete()

    fake = Faker()

    # Create actors
    actors = []
    for _ in range(50):
        actor = Actor(name=fake.name())
        session.add(actor)
        actors.append(actor)
    session.commit()

    # Create movies
    movies = []
    for _ in range(30):
        movie = Movie(title=fake.sentence(), box_office_earnings=random.randint(100000, 1000000))
        session.add(movie)
        movies.append(movie)
    session.commit()

    # Create roles
    for movie in movies:
        for _ in range(20):
            actor = random.choice(actors)
            salary = random.randint(1000, 5000)
            character_name = fake.name()
            role = Role(movie=movie, actor=actor, salary=salary, character_name=character_name)
            session.add(role)
    session.commit()

    session.close()
