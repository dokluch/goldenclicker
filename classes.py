class Counter:
    _instance = None
    _counter = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def counter(self):
        return self._counter

    def increment(self):
        self._counter += 1


