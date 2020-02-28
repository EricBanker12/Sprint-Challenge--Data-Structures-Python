from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.storage = DoublyLinkedList()

    def append(self, item):
        # track current position of tail
        self.current += 1
        if self.current >= self.capacity:
            self.current = 0

        # keep size at or below capacity
        if len(self.storage) >= self.capacity:
            self.storage.remove_from_head()
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if len(self.storage):
            node = self.storage.head
            # append values until node with self.current = 0
            for i in range(len(self.storage) - self.current - 1):
                list_buffer_contents.append(node.value)
                node = node.next
            # insert values 0 to self.current
            for i in range(self.current + 1):
                list_buffer_contents.insert(i, node.value)
                node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.storage = [None for i in range(capacity)]

    def append(self, item):
        self.current += 1
        if self.current >= self.capacity:
            self.current = 0

        self.storage[self.current] = item

    def get(self):
        return [i for i in self.storage if i != None]
    
    # advantage:
    # - less code
    # - no need to add/remove items to keep to capacity
    # - get() is more runtime efficient (O(n) vs O(n^2))
    # disadvantage: 
    # - requires continuous memory
    # special case:
    # - because capacity is constant, there is no issue
    #   with appending/inserting beyond current memory block
