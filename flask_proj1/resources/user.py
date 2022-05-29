from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token
)

from models.user import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help="This field cannot be blank."
)


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"msg": "A user with that username alreadyexists"}, 400
        hashed_password = generate_password_hash(data["password"])
        user = UserModel(data["username"], hashed_password)
        user.save_to_db()
        access_token = create_access_token(identity=user.id, fresh=True)
        return {"msg": "User created successfully", "access_token": access_token}


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data["username"])
        if user is None:
            return {"msg": "Invalid username or password"}, 404
        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)

            return {"msg": "Login success",
                    "access-token": access_token
                    }
