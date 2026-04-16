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
    def insert_after_target(Self,target,data):
        temp = Self.head
        while temp:
            if temp.data == target:
                new_node = node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Target not found")    
    def reverse(Self):
        prev = None
        curr = Self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        Self.head = prev    
    def display(Self):
        temp = Self.head    
        while temp:
            print(temp.data, end = "->")   
            temp = temp.next 
        print("None")    
sll = singly_linked_list()
sll.insert_at_beginning(1)
sll.insert_at_end(2)
sll.insert_after_target(1,3)
sll.insert_after_target(3,4)
sll.reverse()
sll.display()