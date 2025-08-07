class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

# def print__LL(head):
#     while(head!=None):
#         print(head.data)
#         head = head.next

def print__LL(head):
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next

first = Node(10)
second = Node(20)
third = Node(30)

head = first
first.next = second
second.next = third


print__LL(head)