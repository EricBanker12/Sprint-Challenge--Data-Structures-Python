from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # track current position of tail
        if self.current == None:
            self.current = 0
        else:
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
        pass

    def append(self, item):
        pass

    def get(self):
        pass
