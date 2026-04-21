class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linked_list:
    def __init__(self,value):
        new_node = Node(value)   
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    def print(self):
        temp = self.head
        while temp:
            print(temp.value, end = " => ")
            temp = temp.next                    
        print("None")
    def pop(self):
        # print(self.length)
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        while temp.next is not None:
            if temp.next.next == None:
                prev = temp.next
                temp.next = None
                self.tail = temp
                self.length -= 1
                return prev         
            temp = temp.next
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # temp = self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            return temp
    def get(self,target):
        if target < 0 or target >= self.length:
            return None    
        temp = self.head
        index = 0
        while temp:
            if index == target:
                return temp
            temp = temp.next
            index += 1
        return None        
    def set(self,target,value):
        new_node = Node(value)
        if self.get(target) == None:
            return False
        else:
            if target == 0:
                temp = self.head
                new_node.next = self.head.next
                self.head = new_node
                temp.next = None
            else:    
                temp = self.get(target)
                prev = self.get(target - 1)
                new_node.next = temp.next
                prev.next = new_node
                temp.next = None
            return True
            
ll = linked_list(10)   
ll.print()         
ll.append(12)
ll.append(13)
ll.print()
ll.pop()
ll.print()
ll.prepend(19)
ll.print()
ll.pop_first()
ll.print()
print(ll.get(-1))
ll.set(1,50)
ll.print()