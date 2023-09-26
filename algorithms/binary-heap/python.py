from typing import Optional
from heapq import heappush, heappop

class BinaryHeap:

    data : list[int | float]
    minh : bool

    def __init__(self, data: list[int | float] = [], minh: bool = True):
        self.data = []
        self.minh = minh
        for v in data : self.add(v)
    
    def bubble_up(self, i: int):
        while i != 0:
            p = (i - 1) // 2
            if self.minh     and self.data[p] <= self.data[i] : break
            if not self.minh and self.data[p] >= self.data[i] : break
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p

    def bubble_down(self, i: int = 0):
        while True:
            j, l, r = i, 2 * i + 1, 2 * i + 2  # child indices
            if self.minh:
                if l < len(self.data) and self.data[l] < self.data[j] : j = l
                if r < len(self.data) and self.data[r] < self.data[j] : j = r
            else:
                if l < len(self.data) and self.data[l] > self.data[j] : j = l
                if r < len(self.data) and self.data[r] > self.data[j] : j = r
            if i == j : break
            self.data[i], self.data[j] = self.data[j], self.data[i]


    def push(self, value: int | float):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def top(self) -> Optional[int | float]:
        return self.data[0] if self.data else None
    
    def pop(self) -> Optional[int | float]:
        if not self.data       : return None
        if len(self.data) == 1 : return self.data.pop()

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        value = self.data.pop()
        self.bubble_down()
        return value
            

def main():
    
    sequence_min = [1, None, 5,-7, None, 3, None, 2, -2, 12, None, 1, None]
    sequence_max = [1, None, 5,-7, None, 3, None, 2, -2, 12, None, 1, None]

    print("Min Heap:")
    test_heap(sequence_min, True)
    print("Max Heap:")
    test_heap(sequence_max, False)

def test_heap(sequence: list[int | float], minh: bool = True):
    
    bh = BinaryHeap([], minh)  # BinaryHeap 
    py = []                    # python std heap

    for value in sequence:
        if value is None:
            bh_top = bh.pop()
            py_top = heappop(py) * (1 if minh else -1)
            print(f" BinaryHeap: {bh_top}, Python: {py_top}")
            assert bh_top == py_top
        else:
            bh.push(value)
            heappush(py, value * (1 if minh else -1))

if __name__ == "__main__":
    main()
