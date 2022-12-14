from unittest.mock import MagicMock

import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_mock = DirectorDAO(None)

    director_1 = Director(id=1, name="name_1")
    director_2 = Director(id=2, name="name_2")

    director_mock.get_one = MagicMock(return_value=director_1)
    director_mock.get_all = MagicMock(return_value=[director_1, director_2])
    director_mock.create = MagicMock(return_value=director_1)
    director_mock.delete = MagicMock(return_value=True)
    director_mock.update = MagicMock(return_value=True)

    return director_mock

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(1).name == "name_1"

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 2

    def test_delete(self):
        assert self.director_service.delete(1) is True

    def test_update(self):
        assert self.director_service.update(1) is True