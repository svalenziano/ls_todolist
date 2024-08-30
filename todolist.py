from __future__ import annotations

class Todo:

    COMPLETE = '[x]'
    INCOMPLETE = '[ ]'

    def __init__(self, title):
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
        if isinstance(other, Todo):
            return (self.done == other.done) and (self.title == other.title)
        return NotImplemented

class TodoList:
    
    def __init__(self, name):
        self._name = name
        self._todos = []

    def add(self, todo:Todo):
        if isinstance(todo, Todo):
            self._todos.append(todo)
        else:
            class_name = Todo.__class__.__name__
            raise TypeError(f"Requires object of type `{class_name}`")
        
    def __str__(self):
        output_lines = ["---- Today's Todos -----"]
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)



# TESTS ***********************************************************

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list


def step_1():
    print('--------------------------------- Step 1')
    todo_list = setup()

    # setup() uses `todo_list.add` to add 3 todos

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')    # TypeError detected

    for todo in todo_list._todos:
        print(todo)

# step_1()


def step_2():
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

step_2()