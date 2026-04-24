class PrefixTree:
    def __init__(self):
        self.nodes = dict()  # type: ignore

    def insert(self, word: str) -> None:
        curr_d = self.nodes
        for i, c in enumerate(word):
            if curr_d.get(c) is None:
                curr_d[c] = dict()
            curr_d = curr_d[c]
        curr_d[""] = dict()

    def search(self, word: str) -> bool:
        return self.dfs(word, self.nodes)

    def dfs(self, word: str, tree: dict) -> bool:
        if len(word) == 0:
            return tree.get("") is not None

        if tree.get(word[0]) is not None:
            if self.dfs(word[1:], tree[word[0]]):
                return True

        for _, val in tree.items():
            if self.dfs(word, val):
                return True

        return False

    def startsWith(self, prefix: str) -> bool:
        curr_d = self.nodes
        for c in prefix:
            if curr_d.get(c) is None:
                return False
            curr_d = curr_d[c]
        return True

if __name__ == "__main__":
    pt = PrefixTree()
    pt.insert("dog")
    assert pt.search("dog")
    assert not pt.search("do")
    assert pt.startsWith("do")
    pt.insert("do")
    assert pt.search("do")

    pt = PrefixTree()
    pt.insert("app")
    pt.insert("apple")
    assert pt.search("app")
    assert pt.startsWith("apple")
