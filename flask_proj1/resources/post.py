from flask_restful import Resource, reqparse

from models.post import PostModel
from flask import jsonify


class Post(Resource):
    __post__parser = reqparse.RequestParser()
    __post__parser.add_argument(
        "text",
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self, user_id):
        data = Post.__post__parser.parse_args()
        post = PostModel(data["text"], user_id)

        try:
            post.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return post.json(), 201

    def get(self, user_id):
        posts = [posts.json() for posts in PostModel.find_all()]
        if posts:
            return {"posts": posts}
        return {"msg": "No post found"}
