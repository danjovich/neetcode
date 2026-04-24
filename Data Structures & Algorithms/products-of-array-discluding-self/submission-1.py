class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mult = 1
        
        zeros = 0
        for num in nums:
            if num != 0:
                mult *= num
            else:
                zeros += 1

        result = []
        for num in nums:
            if num != 0 and zeros == 0:
                result.append(int(mult / num))
            elif (num != 0 and zeros > 0) or zeros > 1:
                result.append(0)
            elif num == 0 and zeros == 1:
                result.append(mult)
            

        return result

