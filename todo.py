class Todo:
    DONE_MARKER = 'X'
    UNDONE_MARKER = ' '

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    def __str__(self):
        marker = self.DONE_MARKER if self.done else self.UNDONE_MARKER
        return f'[{marker}] {self.title}'

    def __eq__(self, other):
        if isinstance(other, Todo):
            return self.title == other.title and self.done == other.done

        return NotImplemented