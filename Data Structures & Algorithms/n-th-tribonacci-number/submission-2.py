class Solution:
    def tribonacci(self, n: int) -> int:
        prev, curr, next = 0, 0, 1

        for _ in range(n):
            temp = next
            next += prev + curr 
            prev = curr
            curr = temp
        
        return curr
