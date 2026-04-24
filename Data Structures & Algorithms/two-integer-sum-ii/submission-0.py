class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            wanted = target - numbers[i]
            for j in range(i, len(numbers)):
                if numbers[j] > wanted:
                    # since we know numbers in sorted
                    break
                if numbers[j] == wanted:
                    return [i + 1, j + 1]

        return []


if __name__ == "__main__":
    out = Solution().twoSum([1, 2, 3, 4], 3)
    print(out)
    assert out == [1, 2]

    out = Solution().twoSum([1, 2, 3, 4, 8, 10, 32, 56, 78], 36)
    print(out)
    assert out == [4, 7]
