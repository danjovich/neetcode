from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(n) ideal solution
        count = {}
        freqs = [[] for _ in range(len(nums))] # frequency will be at most len(nums)

        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1 # add count to num

        for num, freq in count.items(): # O(n) in worst case
            # the
            freqs[freq - 1].append(num)

        res = []
        for freqs_nums in reversed(freqs): # O(n)
            while len(freqs_nums) > 0: # this will iterate at most k times in all loops
                res.append(freqs_nums.pop())
                if len(res) == k:
                    return res
                
        raise Exception("This code should not be reached")


    #     # O(n * k)
    #     result = []
    #     for _ in range(k):  # O(k)
    #         top_frequent = self.topFrequent(nums) # O(n)
    #         result.append(top_frequent)
    #         nums = [num for num in nums if num != top_frequent]  # O(n)
    #     return result

    # def topFrequent(self, nums: list[int]) -> int:
    #     # O(n)
    #     frequencies = defaultdict(lambda: 0)
    #     for num in nums: # O(n)
    #         frequencies[num] += 1

    #     values = defaultdict(list)
    #     for num, freq in frequencies.items(): # O(n)
    #         values[freq].append(num)

    #     max_freq = max(frequencies.values()) # O(n)
    #     return values[max_freq][0]


if __name__ == "__main__":
    print(Solution().topKFrequent([1, 2, 2, 3, 3, 3], 2))
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent([7, 7], 1))
