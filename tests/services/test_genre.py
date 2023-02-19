from unittest.mock import MagicMock

import pytest

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='Комедия')
    family = Genre(id=2, name='Семейный')
    fantasy = Genre(id=3, name='Фентези')
    drama = Genre(id=4, name='Драма')
    adventure = Genre(id=5, name='Приключения')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, family, fantasy, drama, adventure])
    genre_dao.create = MagicMock(return_value=Genre(id=5))
    genre_dao.update = MagicMock(return_value=Genre(id=4))
    genre_dao.delete = MagicMock(return_value='Ok')

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all(filters=None)

        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "id": 5,
            "name": "Horror"
        }

        genre = self.genre_service.create(genre_d)

        assert genre.id is not None

    def test_update(self):
        genre_d = {
            "id": 5,
            "name": "Horror"
        }

        genre = self.genre_service.update(genre_d)

        assert genre.id is not None

    def test_delete(self):
        delete_completed = self.genre_service.delete(1)

        assert delete_completed is None
