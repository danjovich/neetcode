class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0:
            return x

        if n == 1:
            return x
        
        if n == 0:
            return 1

        n_abs = abs(n)
        pow_of_half = self.myPow(x, n_abs // 2)
        res = pow_of_half * pow_of_half

        if n_abs % 2:
            res *= x

        return res if n > 0 else 1 / res