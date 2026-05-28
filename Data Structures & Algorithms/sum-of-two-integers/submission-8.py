class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            res |= ((a % 2) ^ (b % 2) ^ carry) << i
            carry = ((a % 2) & (b % 2)) | ((a % 2) & (carry % 2)) | ((carry % 2) & (b % 2))

            a //= 2
            b //= 2
            i -= 1
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)
       
        return res
