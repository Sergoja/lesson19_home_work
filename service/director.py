from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, data):
        uid = data.get("id")

        director = self.get_one(uid)

        director.name = data.get("name")

        return self.dao.update(director)

    def delete(self, rid):
        self.dao.delete(rid)