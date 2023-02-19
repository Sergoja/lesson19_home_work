from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    genre_one = Genre(id=1, name='Комедия')
    director_one = Director(id=1, name='Тейлор Шеридан')

    movie_one = Movie(
        id=1,
        title='title1',
        description='description1',
        trailer='https://trailer.com',
        year=1995,
        rating=5,
        genre_id=genre_one,
        director_id=director_one,
    )
    movie_two = Movie(
        id=2,
        title='title2',
        description='description2',
        trailer='https://trailer.com',
        year=2015,
        rating=4,
        genre_id=genre_one.id,
        director_id=director_one,
    )
    movie_three = Movie(
        id=3,
        title='title3',
        description='description3',
        trailer='https://trailer.com',
        year=2005,
        rating=2,
        genre_id=genre_one,
        # genre='hor',
        director_id=director_one,
    )

    movie_dao.get_one = MagicMock(return_value=movie_one)
    movie_dao.get_all = MagicMock(return_value=[movie_one, movie_two, movie_three])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock(return_value='Ok')

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all(filters=None)

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 5,
            "title": "Horror"
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {
            "id": 5,
            "title": "Horror"
        }

        movie = self.movie_service.update(movie_d)
        movie_id = movie.get_one(movie_d.get("id"))

        assert movie_id is not None

    def test_delete(self):
        delete_completed = self.movie_service.delete(1)

        assert delete_completed is None

