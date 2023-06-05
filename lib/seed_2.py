
# Retrieve all actors:
# actors = session.query(Actor).all()


# Retrieve all movies:
# movies = session.query(Movie).all()

# Retrieve all roles:
# roles = session.query(Role).all()

# Retrieve a specific actor by their ID:
# actor = session.query(Actor).get(actor_id)

# Retrieve a specific movie by its ID:
# movie = session.query(Movie).get(movie_id)

# Retrieve all roles for a specific movie:
# movie = session.query(Movie).get(movie_id)
# roles = movie.roles

# Retrieve all actors for a specific movie:
# movie = session.query(Movie).get(movie_id)
# actors = movie.actors

# Retrieve all roles for a specific actor:
# actor = session.query(Actor).get(actor_id)
# roles = actor.roles

# Retrieve all movies that an actor has performed in:
# actor = session.query(Actor).get(actor_id)
# movies = actor.movies

# Retrieve the total salary of a specific actor:
# actor = session.query(Actor).get(actor_id)
# total_salary = actor.total_salary()

# Retrieve the highest-earning actor (based on total salary):
# highest_salary_actor = Actor.most_successful()

# Retrieve all blockbusters (movies with box office earnings over $50,000,000) for a specific actor:
# actor = session.query(Actor).get(actor_id)
# blockbusters = actor.blockbusters()