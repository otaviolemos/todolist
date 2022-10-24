from todoitem import TodoItem
from user import User
from todolist import TodoList

def test_done():
    item = TodoItem('make bed')
    item.complete()
    assert item.is_done() == True

def test_undone():
    item = TodoItem('make bed')
    item.complete()
    item.undo()
    assert item.is_done() == False

def test_change_description():
    item = TodoItem('make bed')
    item.change_description('change bed')
    assert item.description == 'change bed'

def test_one_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    assert list.get(0) == item
    assert list.get_owner() == owner

def test_complete_item_from_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    list.complete_item(0)
    assert item.is_done() == True

def test_remove_item_from_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    list.remove(0)
    assert list.size() == 0

def test_search_item_by_description():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item1 = TodoItem('make bed')
    item2 = TodoItem('withdraw cash')
    list.add(item1)
    list.add(item2)
    assert list.find('withdraw cash') == item2