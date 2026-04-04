class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    
    head = None
    tail = None
    
    for i in range(n):
        value = input(f"Enter value for node {i + 1}: ")
        new_node = Node(value)
        
        if head is None:
            head = new_node
            tail = new_node
        else:
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
    
    temp = head
    while temp is not None:
        print(temp.data, end="")
        if temp.next is not None:
            print(" <->", end="")
        temp = temp.next