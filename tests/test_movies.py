from unittest.mock import MagicMock
import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService

@pytest.fixture
def movie_dao():
    movie_mock = MovieDAO(None)

    movie_1 = Movie(id="1", title="movie_1")
    movie_2 = Movie(id="2", title="movie_2")

    movie_mock.get_one = MagicMock(return_value=movie_1)
    movie_mock.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_mock.create = MagicMock(return_value=movie_1)
    movie_mock.delete = MagicMock(return_value=True)
    movie_mock.update = MagicMock(return_value=True)

    return movie_mock

class TestGenreService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).name == "movie_1"

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_delete(self):
        assert self.movie_service.delete(1) is True

    def test_update(self):
        assert self.movie_service.update(1) is True