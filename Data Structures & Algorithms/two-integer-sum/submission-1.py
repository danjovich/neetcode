class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n)

        # maps values to indexes
        hash_map = {}

        for i, num_i in enumerate(nums):
            nums_j = target - num_i

            # if the current i is the j, it will be found later
            # this also avoids i == j
            if nums_j in hash_map:
                # it's sorted for indexes are increasing
                return [hash_map[nums_j], i]

            hash_map[num_i] = i

        return []

        # old solution: O(n²)
        # for i in range(len(nums)): # n times
        #     expected = target - nums[i]
        #     try:
        #         j = nums.index(expected) # O(n)
        #         if i == j:
        #             continue
        #         return sorted([i, j]) # O(1) sort call
        #     except ValueError:
        #         pass

        # return []


if __name__ == "__main__":
    print(Solution().twoSum([3, 4, 5, 6], 7))
    print(Solution().twoSum([4, 5, 6], 10))
    print(Solution().twoSum([5, 5], 10))
