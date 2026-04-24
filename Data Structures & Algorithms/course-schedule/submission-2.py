from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereqs, unlocks = defaultdict(list), defaultdict(list)

        for c, p in prerequisites:
            if c == p:
                return False
            prereqs[c].append(p)
            unlocks[p].append(c)

        if numCourses == len(unlocks) or numCourses == len(prereqs):
            return False

        def dfs(c: int, visited: set) -> bool:
            if c in visited:
                return False

            visited.add(c)

            for p in prereqs[c]:
                if not dfs(p, visited):
                    return False

            return True

        for p, cs in unlocks.items():
            if len(cs) == 0 and not dfs(c, set()):
                return False

        return True
if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(numCourses, prerequisites, exp):
        res = sol.canFinish(numCourses, prerequisites)
        print(res)
        assert res == exp

    print_and_assert(2, [[0, 1]], True)
    print_and_assert(2, [[0, 1], [1, 0]], False)
    print_and_assert(3, [[0, 2], [1, 2], [2, 0]], False)
