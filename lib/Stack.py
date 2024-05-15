class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if not self.full(): # Important to make sure stack is not full before adding more.
            self.items.append(item)
        else:
            return None # And if it is, then return None.

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        return False

    def search(self, target):
        for i in reversed(range(len(self.items))): # For each reversed number in the range of the length of the items list. Reverse the order is just for efficiency's sake, I think.
            if self.items[i] == target: # If the item at the i'th index is the target
                return len(self.items) -1 -i # Give me the length of the items list minus one minus that i index where the target was found.
        return -1
