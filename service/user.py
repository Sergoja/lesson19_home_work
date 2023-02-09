import base64
import hmac

from dao.user import UserDAO
import hashlib
from configs.config import Config


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_name(self, username):
        return self.dao.get_by_name(username)

    def create(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.update(user_d)

    def delete(self, rid):
        self.dao.delete(rid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def comprare_password(self, hash, password):
        decode_digest = base64.b64decode(hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decode_digest, hash_digest)