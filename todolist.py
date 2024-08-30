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

    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, index:int):
        return self._todos[index]
    
    def mark_done_at(self, index:int):
        self.todo_at(index).done = True

    def mark_undone_at(self, index:int):
        self.todo_at(index).done = False


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

# step_2()


def step_3():
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0

# step_3()

def step_4():
    print('--------------------------------- Step 4')
    todo_list = setup()

    print(todo_list.first())           # [ ] Buy milk
    print(todo_list.last())            # [ ] Go to gym

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')

# step_4()

def step_5():
    print('--------------------------------- Step 5')
    todo_list = setup()

    print(empty_todo_list.to_list())    # []

    todos = todo_list.to_list()
    print(type(todos).__name__)         # list

    for todo in todos:
        print(todo)                     # [ ] Buy milk
                                        # [X] Clean room
                                        # [ ] Go to gym

# step_5()

def step_6():
    print('--------------------------------- Step 6')
    todo_list = setup()

    print(todo_list.todo_at(0))        # [ ] Buy milk
    print(todo_list.todo_at(1))        # [X] Clean room
    print(todo_list.todo_at(2))        # [ ] Go to gym

    try:
        todo_list.todo_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    # Ensure we have a reference
    print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True

# step_6()

def step_7():
    print('--------------------------------- Step 7')
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.mark_done_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [ ] Go to gym

    todo_list.mark_done_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room'
    # [X] Go to gym

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room'
    # [X] Go to gym

    todo_list.mark_undone_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room'
    # [X] Go to gym

    todo_list.mark_undone_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room'
    # [ ] Go to gym

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

step_7()