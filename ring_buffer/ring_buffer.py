class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None for i in range(capacity)]
        self.next_position = -1

    def append(self, item):
        self.buffer[self.get_next_position()] = item

    def get(self):
        return [n for n in self.buffer if n is not None]

    def get_next_position(self):
        self.next_position += 1
        if self.next_position == self.capacity:
            self.next_position = 0
        return self.next_position
