from userrepository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def find_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user