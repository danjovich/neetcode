class MinHeap:
    def __init__(self, nums: list[int]):
        self.heap = [0]
        for num in nums:
            self.push(num)

    def push(self, val: int):
        self.heap.append(val)
        self.heapify_up(len(self))

    def heapify_up(self, i: int):
        if i > 1:
            j = i // 2
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                self.heapify_up(j)

    def heapify_down(self, i: int):
        if 2 * i < len(self.heap):
            j = (2 * i) + 1
            if j >= len(self.heap) or self.heap[j] >= self.heap[j - 1]:
                j -= 1
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                self.heapify_down(j)

    def pop(self) -> int:
        if len(self) > 1:
            minimum = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.heapify_down(1)
            return minimum
        return self.heap.pop()

    def __len__(self) -> int:
        return len(self.heap) - 1

    def __getitem__(self, i: int):
        assert type(i) == int
        return self.heap[i + 1]


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = MinHeap(nums)
        self.k = k
        while len(self.heap) > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap) > self.k:
            self.heap.pop()
        return self.heap[0]


if __name__ == "__main__":
    kl = KthLargest(3, [1, 2, 3, 3])
    assert kl.add(3) == 3
    assert kl.add(5) == 3
    assert kl.add(6) == 3
    assert kl.add(7) == 5
    assert kl.add(8) == 6

    kl = KthLargest(1, [])
    assert kl.add(3) == 3
    assert kl.add(-2) == 3
    assert kl.add(5) == 5
    assert kl.add(10) == 10
    assert kl.add(9) == 10

    kl = KthLargest(4, [4, 5, 5, 6, 6, 7])
    assert kl.add(7) == 6
    assert kl.add(8) == 6
    assert kl.add(5) == 6
    assert kl.add(6) == 6
