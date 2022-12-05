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