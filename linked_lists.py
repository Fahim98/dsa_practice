#linked lists are linear data structure and are slightly different from arrays
#in linked lists, nodes contain data and a pointer(s) (address) to the next node
#this is unlike arrays where every index doesnt have a relation with another index
#arrays are already existing data structures but linked lists are created by us

#types of linked lists

# 1. Singly linked lists - each node has only one address to the next node
# 2. Doubly linked lists - each node has two pointers, one for the previous node and one for the next
# 3. Circular linked lists - same as doubly linked lists but the start and end nodes are also linked to one another forming a closed loop

#implementation (singly)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#creating 4 nodes
node1 = Node(15)
node2 = Node(3)
node3 = Node(17)
node4 = Node(90)

print("The nodes are: ")
print(node1.data)
print(node2.data)
print(node3.data)
print(node4.data)

#linking these nodes (singly)
node1.next = node2
node2.next = node3
node3.next = node4

head = node1 #header node/first node

#traverse and print the linked list
print("Single linked list: ")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


