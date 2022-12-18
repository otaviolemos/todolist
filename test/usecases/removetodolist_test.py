import pytest
from src.usecases.createtodolist import CreateTodoList
from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.errors.invaliduserotnotodolist import InvalidUserOrNoTodoList
from src.usecases.removetodolist import RemoveTodoList
from src.usecases.signup import SignUp
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository


def test_remove_todolist():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    usecase = RemoveTodoList(todolist_repo)
    usecase.perform(user_email)
    no_todo_list = todolist_repo.find_by_email(user_email)
    assert no_todo_list is None

def test_remove_todolist_from_user_without_todolist():
    todolist_repo = InMemoryTodoListRepository()
    user_repo = InMemoryUserRepository()
    user_email = 'joe@doe.com'
    user_name = 'Joe Doe'
    user_password = 'test1234TEST&'
    SignUp(user_repo, FakeHashService()).perform(user_name, user_email, user_password)
    usecase = RemoveTodoList(todolist_repo)
    with pytest.raises(InvalidUserOrNoTodoList):
        usecase.perform(user_email)
