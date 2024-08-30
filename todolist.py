from __future__ import annotations

class Todo:

    COMPLETE = '[x]'
    INCOMPLETE = '[ ]'

    def __init__(self, title):
        Todo.instances.append(self)
        self._title = title
        self.done = False
    
    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._complete
    
    @done.setter
    def done(self, complete:bool):
        if not isinstance(complete, bool):
            raise ValueError('Accepts boolean only')
        self._complete = complete
    
    @property
    def _marker(self):
        return Todo.COMPLETE if self.done else Todo.INCOMPLETE

    def __str__(self):
        return f"{self._marker} {self.title}"
        
    def __eq__(self, other:Todo):
        if not isinstance(other, Todo):
            return NotImplemented
        return (self.done == other.done) and (self.title == other.title)

class TodoList:
    '''
    
    
    '''
    
    
    
    pass


'''
STATE
Title = string
Done = boolean

BEHAVIORS

'''



def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    print(todo1)                  # [ ] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [ ] Clean room

    print(todo2 == todo4)         # True
    print(todo1 == todo2)         # False
    print(todo4.done)             # False

    todo1.done = True
    todo4.done = True
    print(todo4.done)             # True

    print(todo1)                  # [X] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [X] Clean room

    print(todo2 == todo4)         # False

    todo4.done = False
    print(todo4.done)             # False
    print(todo4)                  # [ ] Clean room

test_todo()