class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee in self.follow_map[userId] | {userId}:
            for tweet in self.tweets[followee][-10:]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(reverse=True)
        return [tweet for _, tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
