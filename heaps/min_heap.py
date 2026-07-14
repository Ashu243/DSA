class Min_heap:
    def __init__(self):
        self.arr = []
        self.count = 0

    def heapify_down(self, arr, index):
        smallestidx = index
        leftidx = (2*index)+1
        rightidx = (2*index)+2
        
        n = self.count

        if leftidx < n and arr[leftidx] < arr[index]:
            smallestidx = leftidx
        if rightidx < n and arr[rightidx] < arr[smallestidx]:
            smallestidx = rightidx
        
        if smallestidx != index:
            arr[smallestidx], arr[index] = arr[index], arr[smallestidx]
            self.heapify_down(arr, smallestidx)


    def heapify_up(self, arr, index):
        up_idx = (index-1) // 2

        if up_idx > -1 and arr[up_idx] > arr[index]:
            arr[index], arr[up_idx] = arr[up_idx], arr[index]
            index = up_idx
            self.heapify_up(arr, index)
    
    def initailize_heap(self):
        self.arr.clear()
        self.count = 0

    def insert_elem(self, elem):
        self.arr.append(elem)
        self.heapify_up(self.arr, self.count)
        self.count += 1
    
    def change_key(self, key, index):
        if index < 0 or index >= self.count:
            raise IndexError("Invalid index")
        if self.arr[index] < key:
            self.arr[index] = key
            self.heapify_down(self.arr, index)
        else:
            self.arr[index] = key
            self.heapify_up(self.arr, index)

    def extract_min(self):
        if self.count == 0:
            return None
        self.arr[0], self.arr[self.count-1] = self.arr[self.count-1], self.arr[0]
        ans = self.arr.pop()
        self.count -= 1
        if self.count > 0:
            self.heapify_down(self.arr, 0)
        return ans
    
    def is_empty(self):
        return self.count == 0
    
    def get_min(self):
        return self.arr[0] if self.count > 0 else None
    
    def heapSize(self):
        return self.count
            
