from dao.user import UserDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.auth import AuthService
from service.user import UserService
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from configs.setup_db import db

user_dao = UserDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

user_service = UserService(dao=user_dao)
director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
auth_service = AuthService(user_service)
