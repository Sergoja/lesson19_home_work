import jwt
import datetime
import calendar

from configs.config import Config
from flask import abort

from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(400)
        if not is_refresh:
            if not self.user_service.comprare_password(user.password, password):
                abort(400)

        data = {
            'email': email,
            'role': user.role,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGORITHM)

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def refresh_token(self, token):
        data = jwt.decode(jwt=token, key=Config.SECRET_HERE, algorithms=Config.JWT_ALGORITHM)
        email = data.get('email')

        return self.generate_token(email, None, is_refresh=True)