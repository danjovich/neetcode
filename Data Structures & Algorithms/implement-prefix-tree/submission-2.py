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
        curr_d = self.nodes
        for c in word:
            if curr_d.get(c) is None:
                return False
            curr_d = curr_d[c]
        return curr_d.get("") is not None

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
