# Shubham Arya 1001650536
import heapq
from heapq import heappop, heappush

class Queue:

    # initializes initial value when the class is first called.
    def __init__(self):
        self.queue = []
        self.index = 0

    # pushes the item into queue and increases the index as an item is pushed.
    def insert(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1

    # Removes the item by popping the queue
    def remove(self):
        return heapq.heappop(self.queue)[-1]

    #Sorts the queue in ascending order.
    def sort(self):
        heap = []
        for element in self.queue:
            heappush(heap, element)

        self.queue = []
        while heap:
            self.queue.append(heappop(heap))
