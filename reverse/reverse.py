class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev): #use recursion
        if node is not None:
            curr = node
            next_node = curr.next_node
            curr.next_node = prev
            prev = curr
            self.head = prev
            self.reverse_list(next_node, prev)


    def reverse_list_loop(self, node, prev):
        if node is not None and node.next_node is not None:
            curr = node
            next_node = curr.next_node
            while curr is not None:
                curr.next_node = prev
                prev = curr
                curr = next_node
                if curr is not None:
                     next_node = curr.next_node
            self.head = prev


