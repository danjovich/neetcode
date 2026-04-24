from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.id, tweetId))
        self.id -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = [] + self.tweets[userId]
        for follower in self.follows[userId]:
            tweets += self.tweets[follower]

        heapq.heapify(tweets)

        res = []
        for _ in range(10):
            if not tweets:
                break
            res.append(heapq.heappop(tweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)