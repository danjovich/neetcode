from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [beginWord] + wordList

        n = len(wordList)
        graph = defaultdict(list)
        added_words = 0
        end_word_i = -1

        for curr_word_i in range(n):
            if wordList[curr_word_i] == endWord:
                end_word_i = curr_word_i
            for word_i in range(curr_word_i + 1, n):
                if self.diff(wordList[curr_word_i], wordList[word_i]) == 1:
                    graph[curr_word_i].append(word_i)
                    graph[word_i].append(curr_word_i)
        
        if curr_word_i == -1:
            return 0

        q = deque([(0, 1)])
        visited = {0}
        while q:
            curr, dist = q.popleft()

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    if neighbor == end_word_i:
                        return dist + 1
                    q.append((neighbor, dist + 1))
                    visited.add(neighbor)

        return 0

    def diff(self, w1: str, w2: str) -> int:
        res = abs(len(w1) - len(w1))

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                res += 1

        return res
