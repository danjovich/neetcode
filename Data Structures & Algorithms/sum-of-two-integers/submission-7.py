class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = [0] * 12
        i = 11
        while i >= 0 and (a != 0 or b != 0):
            if i >= 1:
                res[i - 1] ^= ((a % 2) & (b % 2)) | ((a % 2) & (res[i] % 2)) | ((res[i] % 2) & (b % 2))
            res[i] ^= (a % 2) ^ (b % 2)

            print(res)
            
            a //= 2
            b //= 2
            i -= 1
        
        int_res, mult = 0, 1
        neg = res[0] == 1
        for n in reversed(res[1:]):
            if neg:
                n = 1 if n == 0 else 0
            int_res += n * mult
            mult *= 2
        return (int_res + 1) * -1 if neg else int_res
