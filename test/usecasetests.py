from test.inmemoryuserrepository import InMemoryUserRepository
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
from test.fakehashservice import FakeHashService
from test.inmemorytodolistrepository import InMemoryTodoListRepository


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


def test_successful_signin():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    signup = SignUp(user_repo, hash_service)
    signup.perform(user_name, user_email, user_password)
    usecase = SignIn(user_repo, hash_service)
    assert usecase.perform(user_email, user_password) == True


def test_signin_wrong_password():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    signup = SignUp(user_repo, hash_service)
    signup.perform(user_name, user_email, user_password)
    usecase = SignIn(user_repo, hash_service)
    with pytest.raises(InvalidCredentialsError):
        usecase.perform(user_email, 'WRONG_PASSWORD')


def test_signin_invalid_user():
    user_repo = InMemoryUserRepository()
    hash_service = FakeHashService()
    usecase = SignIn(user_repo, hash_service)
    with pytest.raises(InvalidCredentialsError):
        usecase.perform('invalid@user.com', 'any_password')

def test_successful_todolist_creation():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    signup = SignUp(user_repo, hash_service)
    signup.perform(user_name, user_email, user_password)
    usecase = CreateTodoList(user_repo, todolist_repo)
    usecase.perform(user_email)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.size() == 0

def test_todolist_creation_with_invalid_user():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    user_email = "user@not.in.the.system"
    usecase = CreateTodoList(user_repo, todolist_repo)
    with pytest.raises(InvalidUserError):
      usecase.perform(user_email)

def test_duplicate_todolist():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    signup = SignUp(user_repo, hash_service)
    signup.perform(user_name, user_email, user_password)
    usecase = CreateTodoList(user_repo, todolist_repo)
    usecase.perform(user_email)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    with pytest.raises(DuplicateTodoListError):
        usecase.perform(user_email)

def test_create_item_in_todo_list():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    usecase = CreateTodoItem(user_repo, todolist_repo)
    item_description = 'call mom'
    item_priority = 0
    usecase.perform(user_email, item_description, item_priority)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.size() == 1
    assert persisted_todo_list.get(0).description == item_description
    
    