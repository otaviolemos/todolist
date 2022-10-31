from user import User
from duplicateusererror import DuplicateUserError

class SignUp:
    def __init__(self, userrepo, hash_service):
        self.userrepo = userrepo
        self.hash_service = hash_service

    def perform(self, user_name, user_email, user_password):
        if self.userrepo.find_by_email(user_email) != None:
            raise DuplicateUserError()
        hashed_password = self.hash_service.hash(user_password)
        user = User(user_name, user_email, hashed_password)
        self.userrepo.add(user)