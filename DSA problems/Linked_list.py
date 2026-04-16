class node:
    def __init__(Self,data):
        Self.data = data
        Self.next = None

class singly_linked_list:
    def __init__(Self):
        Self.head = None

    def insert_at_beginning(Self,data):
        new_node = node(data)
        new_node.next = Self.head
        Self.head = new_node

    def insert_at_end(Self,data):
        new_node = node(data)
        if not Self.head:
            Self.head = new_node
            return
        temp = Self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node    

    def display(Self):
        temp = Self.head    
        while temp:
            print(temp.data, end = "->")   
            temp = temp.next 
        print("None")    

sll = singly_linked_list()
sll.insert_at_beginning(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.display()