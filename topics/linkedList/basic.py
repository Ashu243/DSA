class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node
    
    def insert_at_position(self, position, value):
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return


        prev_node = None
        current = self.head
        count = 0
        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1

        if prev_node is None:
            print('Position out of Range')
            return
        prev_node.next = new_node
        new_node.next = current

    def delete_node(self, value):
        # case 1 -> if list is empty
        if self.head is None:
            return
        # case 2 if we have to delete first element of linked list
        elif self.head.value == value:
            self.head = self.head.next

        # case 3 -> if we have to delete from middle or last
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next

    def cycle(self):
        current = self.head
        my_set = set()
        while current:
            if current in my_set:
                return True
            my_set.add(current)
            current = current.next
        return False
    
    def cycle_optimal(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
    def cycle_start(self):
        current = self.head
        my_set = set()
        while current:
            if current in my_set:
                return current
            my_set.add(current)
            current = current.next

    def cycle_start_optimal(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
    def remove_from_last(self, n):
        current = self.head
        count = 1
        while current.next:
            current = current.next
            count += 1

        if n == count:
            self.head = self.head.next
        current = self.head
        for i in range(1, count-n):
            current = current.next
        current.next = current.next.next

    def reverse_list(self):
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

    def printlist(self):
        current = self.head

        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('End of list')


ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# ll.insert_at_position(8, 75)
# ll.insert_at_position(-1, 75)
# ll.reverse_list()
ll.remove_from_last(2)
ll.printlist()