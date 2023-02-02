from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def put(self):
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)

        return "", 201
