class MaxHeap:
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
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                self.heapify_up(j)

    def heapify_down(self, i: int):
        if 2 * i < len(self.heap):
            j = (2 * i) + 1
            if j >= len(self.heap) or self.heap[j] < self.heap[j - 1]:
                j -= 1
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                self.heapify_down(j)

    def pop(self) -> int:
        if len(self) > 1:
            maximum = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.heapify_down(1)
            return maximum
        return self.heap.pop()

    def __len__(self) -> int:
        return len(self.heap) - 1

    def __getitem__(self, i: int):
        assert type(i) == int
        return self.heap[i + 1]


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = MaxHeap(stones)
        while len(max_heap) > 1:
            x, y = max_heap.pop(), max_heap.pop()
            diff = abs(x - y)
            if diff != 0:
                max_heap.push(diff)
        return max_heap.pop() if len(max_heap) else 0


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: int):
        res = sol.lastStoneWeight(inp)
        print(res)
        assert res == exp

    print_and_assert([2, 3, 6, 2, 4], 1)
    print_and_assert([1, 2], 1)
