# Linked List
# Removing a node

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def list_print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert_in_middle(self, middle_node, data):
        if middle_node is None:
            print("There is no such a middle node!")
            return
        new_node = Node(data)
        new_node.next = middle_node.next
        middle_node.next = new_node
    
    def remove(self, data):
        previous_node = None
        current_node = self.head
        if current_node is None:
            return
        if current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        while current_node is not None:
            if current_node.data == data:
                break
            previous_node = current_node
            current_node = current_node.next
        if current_node == None:
            return
        else:
            previous_node.next = current_node.next
            current_node = None
            

# Todo list test
todo_node0 = Node("BRUNCH")
todo_node1 = Node("BOCCE")
todo_node2 = Node("DRINK TEA")

todo_list = LinkedList()
todo_list.head = todo_node0
todo_node0.next = todo_node1
todo_node1.next = todo_node2

todo_list.remove("BOCCE")

todo_list.list_print()
