from inmemoryuserrepository import InMemoryUserRepository
from signup import SignUp
import pytest
from duplicateusererror import DuplicateUserError
from fakehashservice import FakeHashService

def test_signup_with_valid_data():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    usecase = SignUp(user_repo, hash_service)
    usecase.perform(user_name, user_email, user_password)
    assert user_repo.find_by_email(user_email).name == user_name

def test_prevent_duplicate_user():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    usecase = SignUp(user_repo, hash_service)
    usecase.perform(user_name, user_email, user_password)
    dup_user_name = 'Doe Joe'
    dup_user_email = 'joe@doe.com'
    dup_user_password = 'TEST1234test&'
    with pytest.raises(DuplicateUserError):
        usecase.perform(dup_user_name, dup_user_email, dup_user_password)

def test_hash_password():
    user_repo = InMemoryUserRepository()
    hash_service = BcryptHashService(bcrypt.gensalt(14))
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    usecase = SignUp(user_repo, hash_service)
    usecase.perform(user_name, user_email, user_password)
    saved_user = user_repo.find_by_email(user_email)
    assert saved_user.name == user_name
    assert saved_user.password != user_password
    assert hash_service.check(user_password, saved_user.password)