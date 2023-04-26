class Counter:
    def __init__(self, class_id, text):
        self._counter = 0
        self.text = text
    
    @property
    def counter(self):
        return self._counter
    
    def increment(self):
        self._counter += 1

    def __str__(self):
        return f"{self.text} clicked: {self._counter}"


