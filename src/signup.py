from user import User

class SignUp:
    def __init__(self, userrepo):
        self.userrepo = userrepo

    def perform(self, user_name, user_email, user_password):
        user = User(user_name, user_email, user_password)
        self.userrepo.add(user)