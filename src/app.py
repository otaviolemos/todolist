import bcrypt
from flask import Flask, request, jsonify
from src.externals.bcrypthashservice import BcryptHashService
from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from src.usecases.signup import SignUp



def create_app():
    app = Flask(__name__)
    salt = bcrypt.gensalt()
    user_repo = InMemoryUserRepository()
    hash_service = BcryptHashService(salt)

    @app.route("/api/users", methods = ['POST'])
    def signup():
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        signup_usecase = SignUp(user_repo, hash_service)
        try:
          signup_usecase.perform(name, email, password)
        except Exception as error:
          return jsonify({
            "error": str(error)
          }), 400
        result = { 
          "name": name,
          "email": email 
        }
        return jsonify(result), 201

    return app