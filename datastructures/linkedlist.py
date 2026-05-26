class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, data):

        node = Node(data)

        if self.head is None:

            self.head = node
            return

        current = self.head

        while current.next:

            current = current.next

        current.next = node

    def remove(self, target):

        if self.head is None:

            return False

        if self.head.data == target:

            self.head = self.head.next
            return True

        current = self.head

        while current.next:

            if current.next.data == target:

                current.next = current.next.next
                return True

            current = current.next

        return False

    def search(self, target):

        current = self.head

        while current:

            if current.data == target:

                return current.data

            current = current.next

        return None

    def to_list(self):

        result = []

        current = self.head

        while current:

            result.append(current.data)

            current = current.next

        return result
