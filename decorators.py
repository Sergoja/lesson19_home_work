from flask import request
from flask_restx import abort
import jwt

from config import Config


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, Config.SECRET_HERE, algorithms=Config.JWT_ALGORITHM)
        except Exception as e:
            print('JWR Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer')[-1]

        try:
            user = jwt.decode(token, Config.SECRET_HERE, algorithms=[Config.JWT_ALGORITHM])
            if user['role'] != 'admin':
                return 'You are not admin'
        except Exception as e:
            print('JWR Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper