from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from configs.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        res = UserSchema(many=True).dump(users)
        return res, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)

        return "", 201, {'location': f'/users/{user.id}'}


@user_ns.route('/<int:rid>')
class UserView(Resource):
    def get(self, rid):
        user = user_service.get_one(rid)
        sm_d = UserSchema().dump(user)
        return sm_d, 200

    def put(self, rid):
        req_json = request.json
        req_json["id"] = rid
        user_service.update(req_json)

        return "", 204

    def delete(self, rid):
        user_service.delete(rid)

        return "", 204