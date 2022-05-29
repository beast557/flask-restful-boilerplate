from flask import Flask
from flask_restful import Api
from db import db
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, UserLogin
from resources.post import Post

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nepal980@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, "/signup")
api.add_resource(UserLogin, "/login")
api.add_resource(Post, '/post/<int:user_id>')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
