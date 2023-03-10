from flask import request
from flask_restx import Resource, Namespace

from configs.implemented import auth_service, user_service

auth_ns = Namespace('auth')


# @auth_ns.route('/')
# class AuthView(Resource):
#     def put(self):
#         req_json = request.json
#
#         token = req_json.get('refresh_token')
#
#         if token is None:
#             return 400
#
#         tokens = auth_service.refresh_token(token)
#
#         return tokens, 201

    # def post(self):
    #     req_json = request.json
    #
    #     username = req_json.get('username')
    #     password = req_json.get('password')
    #
    #     if None in [username, password]:
    #         return 400
    #
    #     tokens = auth_service.generate_token(username, password)
    #
    #     return tokens, 201


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)

        return 201


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get('email')
        password = req_json.get('password')

        if not email or not password:
            return 400

        tokens = auth_service.generate_token(email, password)

        return tokens, 201

    def put(self):
        req_json = request.json

        token = req_json.get('refresh_token')

        if token is None:
            return 400

        tokens = auth_service.refresh_token(token)

        return tokens, 201
