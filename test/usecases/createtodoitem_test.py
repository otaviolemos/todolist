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
from src.entities.errors.duplicateitemerror import DuplicateItemError
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository

def test_create_item_in_todo_list():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    usecase = CreateTodoItem(todolist_repo)
    item_description = 'call mom'
    item_priority = 0
    usecase.perform(user_email, item_description, item_priority)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.size() == 1
    assert persisted_todo_list.get(0).description == item_description

def test_create_item_in_todo_list_with_invalid_user():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@user.com'
    usecase = CreateTodoItem(todolist_repo)
    item_description = 'call mom'
    item_priority = 0
    with pytest.raises(InvalidUserError):
        usecase.perform(user_email, item_description, item_priority)

def test_create_duplicate_item_in_todo_list():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    usecase = CreateTodoItem(todolist_repo)
    item_description = 'call mom'
    item_priority = 0
    usecase.perform(user_email, item_description, item_priority)
    with pytest.raises(DuplicateItemError):
        usecase.perform(user_email, item_description, item_priority)
