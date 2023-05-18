# Homework
# Problem 1: Add a .remove method to the LinkedList
# Add a method to the LinkedList class to remove a node from the list.

# The method should take in a string of the value to remove and remove the node with that value from the LinkedList.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def get_node(self, value_to_get):
        check = self.head
        while check is not None:
            if check.value == value_to_get:
                return check
            check = check.next
        return None
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def insert_after(self, prev_value, new_value):
        prev_node = self.get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
            return
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def traverse_list(self):
        node = self.head
        while node:
            print(node) 
            node = node.next
    
    def remove(self, value_to_remove): 
        
        previous_node = self.head
        next = self.head.next
        
        while next is not None:
            if next.value == value_to_remove: # pop doesnt work for wed, only to pop off end of array or linked list
                # next.pop
                previous_node.next = next.next # Node matches, so remove it and update the links, aka: a->b->c to a->c
                return
            
            previous_node = next
            next = next.next

        print(f"{value_to_remove} item not found")

# note: This code below doesnt run
    # def remove(self, key):
    #     temp = self.head # Keep temp head location
    #     if temp is not None and temp.data == key: # If key found delete node
    #         self.head = temp.next
    #         temp = None
    #         return
    #     while temp is not None and temp.data != key: # Look for node by key
    #         prev = temp
    #         temp = temp.next
    #     prev.next = temp.next # Switch current node with previous 
    #     temp = None #Remove node
    
                
    
weekdays = LinkedList()  # Sunday is the head/ Saturday is the tail
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

weekdays.remove('Wednesday')

weekdays.traverse_list()


# Sunday
# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday