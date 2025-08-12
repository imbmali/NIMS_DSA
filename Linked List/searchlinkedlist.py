class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return f"Found {key} at position {position}"
            current = current.next
            position += 1
        return f"{key} not found"

# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll.search(20))  # Found 20 at position 1
print(ll.search(50))  # 50 not found
