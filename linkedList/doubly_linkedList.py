class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_in_between(self, value, position):
        new_node = Node(value)
        if position == 0:
            self.insert_at_head(value)
            return
        current = self.head
        count = 1
        while current and count < position:
            current = current.next
            count += 1
        if current is None:
            print("position out of bound")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            next = current.next
            current.prev = next
            current.next = prev_node
            prev_node = current
            current = next
    
    def insert_at_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_all_occ(self, key):
        current = self.head
        prev = None
        while current:
            front = current.next
            if current.value == key:
                if current.prev:
                    prev.next = front
                    if front:
                        front.prev = prev
                else:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
            else:
                prev = current
            current = front
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print("None")
            
    # def findPairsWithGivenSum(self, target):
    #     current = self.head
    #     my_set = set()
    #     result = []
    #     while current:
    #         diff = target - current.value
    #         if diff in my_set:
    #             result.append([diff, current.value])
    #         my_set.add(current.value)
    #         current = current.next
    #     return result

    def findPairsWithGivenSumOptimal(self, target):
        left = self.head
        right = self.head
        result = []
        while right.next:
            right = right.next

        while left.value < right.value:
            sum = left.value + right.value
            if sum == target:
                result.append([left.value, right.value])
                left = left.next
                right = right.prev
            elif sum > target:
                right = right.prev
            else:
                left = left.next
        
        return result

    def remove_duplicates(self):
        current = self.head
        while current:
            if current.prev and current.value == current.prev.value:
                if current.prev ==  self.head:
                    current.prev = None
                    self.head = current
                else:
                    current.prev.prev.next = current
                    current.prev = current.prev.prev
            current = current.next
        
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # without using tail
        # else:
        #     current = self.head
        #     while current.next:
        #         current = current.next
        #     current.next = new_node
        #     new_node.prev = current

        # using tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    


dll = Doubly_linked_list()
dll.append(10)
dll.append(10)
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(40)
dll.append(50)
dll.append(60)
dll.append(60)
dll.append(60)
dll.append(70)
dll.append(80)
# dll.insert_in_between(10, 3)
# dll.delete_all_occ(80)
dll.remove_duplicates()
dll.print_list()

# print(dll.findPairsWithGivenSum(70))
# print(dll.findPairsWithGivenSumOptimal(70))