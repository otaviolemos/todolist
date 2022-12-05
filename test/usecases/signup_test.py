from src.usecases.signup import SignUp
from src.usecases.signin import SignIn
from src.usecases.createtodolist import CreateTodoList
from src.usecases.createtodoitem import CreateTodoItem
import pytest
from src.usecases.errors.duplicateusererror import DuplicateUserError
from src.usecases.errors.invalidpassworderror import InvalidPasswordError
from src.usecases.errors.invalidcredentialserror import InvalidCredentialsError
from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.errors.duplicatetodolisterror import DuplicateTodoListError
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository


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
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    usecase = SignUp(user_repo, hash_service)
    usecase.perform(user_name, user_email, user_password)
    saved_user = user_repo.find_by_email(user_email)
    assert saved_user.name == user_name
    assert saved_user.password != user_password
    assert hash_service.check(user_password, saved_user.password)


def test_password_lowercase_letter():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'TEST1234TEST&'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)


def test_password_uppercase_letter():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234test&'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)


def test_password_number():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'testTESTtest&'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)


def test_password_special_character():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'testTESTtest1'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)


def test_password_too_short():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'aA1$T'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)


def test_password_too_long():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'aA1$TaA1$TaA1$TT'
    usecase = SignUp(user_repo, hash_service)
    with pytest.raises(InvalidPasswordError):
        usecase.perform(user_name, user_email, user_password)