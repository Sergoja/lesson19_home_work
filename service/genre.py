from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, data):
        uid = data.get("id")

        genre = self.get_one(uid)

        genre.name = data.get("name")

        return self.dao.update(genre)

    def delete(self, rid):
        self.dao.delete(rid)
