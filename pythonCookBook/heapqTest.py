import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, Item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

    def print_item(self):
        print(self.name)


# q = PriorityQueue()
# q.push(Item('xiaoi'), 1)
# q.push(Item('xiao'), 2)
# q.push(Item('xia'), 4)
# q.push(Item('xi'), 3)


Item('sdf').print_item()
