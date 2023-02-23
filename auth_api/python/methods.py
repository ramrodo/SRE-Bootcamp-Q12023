import hashlib
import jwt
from flask import abort

from db import Database

db_conn = Database()

class Token:

    def generate_token(self, username, password):
        user = db_conn.getUser(username)
        user_username = user[0]
        user_password = user[1]
        user_salt = user[2]
        user_role = user[3]

        hashed_password = self.validate_password(password, user_salt)

        if user_password == hashed_password:
            payload = {"username": user_username, "role": user_role, }
            token = jwt.encode(payload, db_conn.getEncryptToken(), algorithm="HS256")
            return token
        else:
            return "Invalid password"

    def validate_password(self, password, salt):
        password_salt = password + salt
        hash = hashlib.sha512(password_salt.encode("utf-8")).hexdigest()
        return hash


class Restricted:

    def is_user_allowed(self, username, role):
        user = db_conn.getUser(username)
        user_username = user[0]
        user_role = user[3]
        if username == user_username and role == user_role:
            return True
        return False

    def access_data(self, token):
        try:
            data_decoded = jwt.decode(token[7:], db_conn.getEncryptToken(), algorithms=["HS256"])
            if self.is_user_allowed(data_decoded["username"], data_decoded["role"]):
                return "You are under protected data"
            return "You are not allowed"
        except:
            return "You are under protected data"
