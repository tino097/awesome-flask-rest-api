from app.blueprints import user_pb
from flask_restx import Api, Resource


api = Api(user_pb, doc="/docs")
user_ns = api.namespace("user", description="User CRUD operations")

@user_ns.route("/")
class UserList(Resource):
    def get(self):
        """
        Returns list of users
        """
        return "Hello"

    def post(self):
        """
        Create new user and adds to the list
        """

@user_ns.route("/<int:id>")
class User(Resource):
    def get(self, id):
        """
        Displays a user's details
        """

    def put(self, id):
        """
        Updates a user's details
        """

    def delete(self, id):
        """
        Delete a user and removes from the list
        """