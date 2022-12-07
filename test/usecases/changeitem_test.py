import pytest
from src.entities.priority import Priority
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from src.usecases.createtodoitem import CreateTodoItem
from src.usecases.createtodolist import CreateTodoList
from src.usecases.signup import SignUp
from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.changeitem import ChangeItem, ChangeType


def test_change_item_description():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    item_description = 'call mom'
    item_priority = 0
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    CreateTodoItem(todolist_repo).perform(user_email, item_description, item_priority)
    new_description = 'call dad'
    usecase = ChangeItem(todolist_repo)
    usecase.perform(user_email, item_description, ChangeType.DESCRIPTION, new_description)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.size() == 1
    assert persisted_todo_list.get(0).description == new_description

def test_change_item_description_with_invalid_user():
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@user.com'
    item_description = 'call mom'
    new_description = 'call dad'
    usecase = ChangeItem(todolist_repo)
    with pytest.raises(InvalidUserError):
      usecase.perform(user_email, item_description, ChangeType.DESCRIPTION, new_description)

def test_change_item_priority():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    item_description = 'call mom'
    item_priority = Priority.LOW
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    CreateTodoItem(todolist_repo).perform(user_email, item_description, item_priority)
    new_priority = Priority.MEDIUM
    usecase = ChangeItem(todolist_repo)
    usecase.perform(user_email, item_description, ChangeType.PRIORITY, new_priority)
    persisted_todo_list = todolist_repo.find_by_email(user_email)
    assert persisted_todo_list.size() == 1
    assert persisted_todo_list.get(0).priority == new_priority

def test_change_item_priority_with_invalid_user():
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@user.com'
    item_description = 'call mom'
    new_priority = Priority.HIGH
    usecase = ChangeItem(todolist_repo)
    with pytest.raises(InvalidUserError):
      usecase.perform(user_email, item_description, ChangeType.PRIORITY, new_priority)