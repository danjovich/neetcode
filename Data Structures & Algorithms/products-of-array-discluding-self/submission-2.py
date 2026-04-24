# TODO: O(n) without division
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # idea: use prefix and postfix array
        # example: [  1,  2,  3,  4 ]
        # prefix:  [  1,  2,  6, 24 ]   (multiplying each number with the ones before)
        # postfix: [ 24, 24, 12,  4 ] (like prefix, but from the end to the start)
        # Then the result is for each index i if prefix[i-1] * postfix[i+1]
        # O(n)

        res = []
        pref = 1
        post = 1

        for i in range(len(nums)):
            if i > 0:
                pref *= nums[i-1]
            res.append(pref)

        for i in reversed(range(len(nums))):
            if i < len(nums) - 1:
                post *= nums[i + 1]
            res[i] *= post
        
        return res
                


    def productExceptSelfWithDivision(self, nums: list[int]) -> list[int]:
        # time: O(n), space: O(1) (the answer itself doesn't count)
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


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 4, 6]))
    assert Solution().productExceptSelf([1, 2, 4, 6]) == [48, 24, 12, 8]

    print(Solution().productExceptSelf([-1, 0, 1, 2, 3]))
    assert Solution().productExceptSelf([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]

    print(Solution().productExceptSelf([-1, 0, 0, 2, 3]))
    assert Solution().productExceptSelf([-1, 0, 0, 2, 3]) == [0, 0, 0, 0, 0]
