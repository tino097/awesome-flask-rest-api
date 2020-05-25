from app.blueprints import company_bp
from flask_restx import Api, Resource


api = Api(company_bp, doc="/docs")
company_ns = api.namespace("company", description="Company CRUD operations")


@company_ns.route("/")
class CompanyList(Resource):
    def get(self):
        """
        Returns list of companies
        """
        return "Hello"

    def post(self):
        """
        Create new company and adds to the list
        """


@company_ns.route("/<int:id>")
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
