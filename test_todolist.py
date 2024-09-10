import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], 
                         self.todos.to_list())
        
    def test_first(self):
        self.assertIs(self.todo1, self.todos.first())

    def test_last(self):
        self.assertIs(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add('This is not a Todo object')
        with self.assertRaises(TypeError):
            self.todos.add(1234)
        with self.assertRaises(TypeError):
            another_list = TodoList('tktk')
            self.todos.add(another_list)

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(self.todo2, self.todos.todo_at(1))
        with self.assertRaises(IndexError):
            self.todos.todo_at(666)
        with self.assertRaises(TypeError):
            self.todos.todo_at('NaN')

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        self.assertEqual(self.todo1.done, True)
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(666)
        with self.assertRaises(TypeError):
            self.todos.mark_done_at('NaN')

    def test_mark_undone_at(self):
        self.assertEqual(self.todo1.done, False)
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done)
        for idx in range(len(self.todos)):
            self.todos.mark_undone_at(idx)
        self.assertFalse(self.todos.all_done())

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(666)

    def test_mark_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(all([self.todo1.done,
                             self.todo2.done,
                             self.todo3.done]))
        
    def test_remove_at(self):
        length = len(self.todos)
        self.todos.remove_at(0)
        self.assertEqual(length - 1, len(self.todos))

        with self.assertRaises(IndexError):
            self.todos.remove_at(666)
        
        with self.assertRaises(TypeError):
            self.todos.remove_at('not a number')

    def test_str(self):
        expected = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(expected, str(self.todos))

    def test_str_done_todo(self):
        expected = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )
        self.todos.mark_done_at(1)
        self.assertEqual(expected, str(self.todos))

    def test_str_all_done_todos(self):
        expected = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        self.todos.mark_all_done()
        self.assertEqual(expected, str(self.todos))
    
    def test_each(self):
        self.assertFalse(self.todos.all_done())
        def callback(todo:Todo):
            todo.done = True
        self.todos.each(callback)
        self.assertTrue(self.todos.all_done())

    def test_select(self):
        def contains_a_y(todo:Todo):
            return 'y' in str(todo)
        sublist = self.todos.select(contains_a_y)
        expected = TodoList(self.todos.title)
        expected.add(self.todo1)
        expected.add(self.todo3)
        # print(); print(sublist.title); print(sublist)
        # print(expected.title); print(expected)
        self.assertEqual(expected.to_list(), sublist.to_list())

if __name__ == "__main__":
    unittest.main()