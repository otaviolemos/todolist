from src.entities.todoitem import TodoItem
from src.entities.user import User
from src.entities.priority import Priority

def test_done():
    item = TodoItem('make bed', Priority.LOW)
    item.complete()
    assert item.is_completed() == True

def test_undone():
    item = TodoItem('make bed', Priority.LOW)
    item.complete()
    item.undo()
    assert item.is_completed() == False

def test_change_description():
    item = TodoItem('make bed', Priority.LOW)
    item.change_description('change bed')
    assert item.description == 'change bed'