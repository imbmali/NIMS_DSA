class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, go to the last node and link the new one
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.print_list()  # 10 -> 20 -> 30 -> None
