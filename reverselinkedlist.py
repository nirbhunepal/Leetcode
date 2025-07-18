class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def print_list(node):
    while node:
        print(node.data, end=" → ")
        node = node.next
    print("None")
print_list(head)

def reverse_list(head):
    current = head
    prev = None
    
    while current:
        next_item = current.next
        current.next = prev
        prev = current
        current = next_item
    return prev
    
a = reverse_list(head)
print_list(a)