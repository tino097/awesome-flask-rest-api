from flask import Flask, Blueprint
from flask_restplus import Api, Resource

app = Flask(__name__)
blueprint = Blueprint("company", __name__)
api = Api(blueprint, doc="/docs")
namespace_conf = api.namespace("companies", description="Company CRUD operations")


app.register_blueprint(blueprint, url_prefix="/companies")

app.run(debug=True)


@namespace_conf.route("/")
class CompanyList(Resource):
    def get(self):
        """
        Returns list of companies
        """

    def post(self):
        """
        Create new company and adds to the list
        """


@namespace_conf.route("/<int:id>")
class Company(Resource):
    def get(self, id):
        """
        Displays a company's details
        """

    def put(self, id):
        """
        Updates a company's details
        """

    def delete(self, id):
        """
        Delete a company and removes from the list
        """

