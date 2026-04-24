from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereqs, unlocks = defaultdict(list), [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            if c == p:
                return False
            prereqs[c].append(p)
            unlocks[p].append(c)

        if numCourses == len(prereqs):
            return False

        global_visited = set()
        def dfs(c: int, visited: set) -> bool:
            if c in visited:
                return False
            
            if c in global_visited:
                return True

            visited.add(c)

            for p in prereqs[c]:
                if not dfs(p, visited):
                    return False

            global_visited.add(c)
            visited.remove(c)
            return True

        unlocks_count = 0
        for p, cs in enumerate(unlocks):
            if len(cs) == 0 and not dfs(p, set()):
                return False
            if len(cs) != 0:
                unlocks_count += 1

        return len(global_visited) == numCourses and unlocks_count != numCourses


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(numCourses, prerequisites, exp):
        res = sol.canFinish(numCourses, prerequisites)
        print(res)
        assert res == exp

    print_and_assert(2, [[0, 1]], True)
    print_and_assert(2, [[0, 1], [1, 0]], False)
    print_and_assert(3, [[0, 2], [1, 2], [2, 0]], False)
    print_and_assert(4, [[0, 1], [3, 1], [1, 3], [3, 2]], False)
    print_and_assert(5, [[1, 4], [2, 4], [3, 1], [3, 2]], True)
    print_and_assert(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]], False)
