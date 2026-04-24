from math import inf


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        for _ in range(k):
            top_frequent = self.topFrequent(nums)
            result.append(top_frequent)
            nums = [num for num in nums if num != top_frequent]
        return result

    def topFrequent(self, nums: list[int]) -> int:
        biggest_frequency = -inf
        most_frequent = None
        checked = {num: False for num in nums}
        for num in nums:
            if checked[num]:
                continue
            checked[num] = True
            count = nums.count(num)
            if count > biggest_frequency:
                biggest_frequency = count
                most_frequent = num
        return most_frequent
