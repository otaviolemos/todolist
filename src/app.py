import bcrypt
from flask import Flask, request, jsonify
from src.externals.bcrypthashservice import BcryptHashService
from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from src.usecases.signup import SignUp



def create_app():
    app = Flask(__name__)

    @app.route("/api/users", methods = ['POST'])
    def signup():
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        salt = bcrypt.gensalt()
        hash_service = BcryptHashService(salt)
        user_repo = InMemoryUserRepository()
        signup_usecase = SignUp(user_repo, hash_service)
        signup_usecase.perform(name, email, password)
        result = { 
          "name": name,
          "email": email 
        }
        return jsonify(result), 201

    return app