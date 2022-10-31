from hashservice import HashService

class FakeHashService(HashService):
    def __init__(self):
        pass

    def hash(self, password):
        return password + 'HASHED'

    def check(self, password, hashed):
        if hashed == password + 'HASHED':
            return True
        return False