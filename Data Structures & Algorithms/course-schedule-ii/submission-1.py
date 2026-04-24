from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prereqs_dict = defaultdict(list)

        for prereq in prerequisites:
            prereqs_dict[prereq[0]].extend(prereq[1:])

        res, res_set = [], set()

        def dfs(course: int, visited: set) -> bool:
            if course in res_set:
                return True
            
            if not prereqs_dict[course]:
                res.append(course)
                res_set.add(course)
                visited.add(course)
                return True

            if course in visited:
                return False
                

            visited.add(course)
            curr_visited = visited.copy()

            for prereq in prereqs_dict[course]:
                if prereq in visited and prereq not in curr_visited:
                    continue

                if not dfs(prereq, visited):
                    return False

            res.append(course)
            res_set.add(course)
            return True

        visited = set()
        for course in range(numCourses):
            local_visited = set()
            if course not in visited and not dfs(course, local_visited):
                return []
            visited.update(local_visited)

        return res