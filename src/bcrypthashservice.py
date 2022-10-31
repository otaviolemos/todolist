import bcrypt

class BcryptHashService():
    def __init__(self, salt):
        self.salt = salt

    def hash(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.salt)

    def check(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    