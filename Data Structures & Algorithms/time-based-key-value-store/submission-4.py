from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l, r = 0, len(values) - 1

        while r - l > 1:
            m = (l + r) // 2
            t, v = values[m]

            if t == timestamp:
                return v
            elif t > timestamp:
                r = m
            else:
                l = m

        if r > 0 and values[r][0] <= timestamp:
            return values[r][1]

        if l < len(values) and values[l][0] <= timestamp:
            return values[l][1]

        return ""


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("alice", "happy", 1)
    assert tm.get("alice", 1) == "happy"
    assert tm.get("alice", 2) == "happy"
    assert tm.get("alice", 0) == ""
    tm.set("alice", "sad", 3)
    assert tm.get("alice", 3) == "sad"

    tm = TimeMap()
    tm.set("key1", "value1", 10)
    assert tm.get("key1", 1) == ""
    assert tm.get("key1", 10) == "value1"
    assert tm.get("key1", 11) == "value1"

    tm = TimeMap()
    tm.set("test", "one", 10)
    tm.set("test", "two", 20)
    tm.set("test", "three", 30)
    assert tm.get("test", 15) == "one"
    assert tm.get("test", 25) == "two"
    assert tm.get("test", 35) == "three"
