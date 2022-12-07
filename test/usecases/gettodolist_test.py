import pytest
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository
from src.usecases.createtodolist import CreateTodoList
from src.usecases.gettodolist import GetTodoList
from src.usecases.signup import SignUp
from src.usecases.errors.invalidusererror import InvalidUserError


def test_succesful_todolist_retrieval():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    signup = SignUp(user_repo, hash_service)
    signup.perform(user_name, user_email, user_password)
    createtodolist = CreateTodoList(user_repo, todolist_repo)
    createtodolist.perform(user_email)
    usecase = GetTodoList(todolist_repo)
    retrieved_todo_list = usecase.perform(user_email)
    assert retrieved_todo_list.size() == 0
    assert todolist_repo.find_by_email(user_email) != None

def test_succesful_todolist_retrieval():
    todolist_repo = InMemoryTodoListRepository()
    user_email = 'invalid@user.com'
    usecase = GetTodoList(todolist_repo)
    with pytest.raises(InvalidUserError):
        usecase.perform(user_email)