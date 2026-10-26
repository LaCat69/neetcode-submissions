class Twitter:

    def __init__(self):
        self.time = 0
        self.users_follows = defaultdict(set)
        self.user_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        if self.user_tweets[userId]:
            heapq.heappush_max(heap, (self.user_tweets[userId][-1][0], 
            self.user_tweets[userId][-1][1], 
            userId, 
            len(self.user_tweets[userId])-1))
        for f in self.users_follows[userId]:
            if self.user_tweets[f]:
                heapq.heappush_max(heap, (self.user_tweets[f][-1][0], 
                self.user_tweets[f][-1][1], f, len(self.user_tweets[f])-1))

        while len(res) != 10 and heap:
            _, tweet_id, user, index = heapq.heappop_max(heap)
            if index > 0:
                heapq.heappush_max(heap, (self.user_tweets[user][index-1][0], 
                self.user_tweets[user][index-1][1], 
                user, 
                index-1))
            res.append(tweet_id)

        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_follows[followerId].discard(followeeId)
        