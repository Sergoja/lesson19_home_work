from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    teilor = Director(id=1, name='Тейлор Шеридан')
    quentin = Director(id=2, name='Квентин Тарантино')
    vladimir = Director(id=3, name='Владимир Вайншток')
    dekster = Director(id=4, name='Декстер Флетчер')
    stive = Director(id=5, name='Стив Энтин')

    director_dao.get_one = MagicMock(return_value=teilor)
    director_dao.get_all = MagicMock(return_value=[teilor, quentin, vladimir, dekster, stive])
    director_dao.create = MagicMock(return_value=Director(id=5))
    director_dao.update = MagicMock(return_value=Director(id=4))
    director_dao.delete = MagicMock(return_value='Ok')

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "id": 5,
            "name": "Jhon"
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 5,
            "name": "Jhon"
        }

        director = self.director_service.update(director_d)

        assert director.id is not None

    def test_delete(self):
        delete_completed = self.director_service.delete(1)

        assert delete_completed is None
