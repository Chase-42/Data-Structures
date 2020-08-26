class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        #not sure why storage and not size?
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        #why do you need a conditional here??
        if len(self.storage) > 0:
            return self.storage.pop()