from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from configs.implemented import user_service
from decorators import auth_required, admin_required

user_ns = Namespace('user')


# @user_ns.route('/')
# class UsersView(Resource):
#     def get(self):
#         users = user_service.get_all()
#         res = UserSchema(many=True).dump(users)
#         return res, 200
#
#     def patch(self):
#         req_json = request.json
#         user = user_service.create(req_json)
#
#         return "", 201, {'location': f'/users/{user.id}'}


@user_ns.route('/<int:rid>')
class UserView(Resource):
    @auth_required
    def get(self, rid):
        user = user_service.get_one(rid)
        sm_d = UserSchema().dump(user)
        return sm_d, 200

    @auth_required
    def patch(self, rid):
        req_json = request.json
        req_json["id"] = rid
        user_service.update(req_json)

        return "", 204

    @admin_required
    def delete(self, rid):
        user_service.delete(rid)

        return "", 204


@user_ns.route('/password/<int:rid>')
class UserView(Resource):
    @auth_required
    def put(self, rid):
        req_json = request.json
        password_1 = req_json.get('password')
        password_2 = req_json.get('password_2')
        user = user_service.get_one(rid)

        if user_service.get_hash(password_1) != user.password:
            return 400

        user.password = password_2
        user_service.update(user)

        return 200
