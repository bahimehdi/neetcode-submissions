from itertools import islice

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            if userId not in self.tweets:
                return []
            newsFeed = self.tweets[userId][-10:][::-1]
            return [tweetId for _, tweetId in newsFeed]

        tweets = list()
        if userId in self.tweets:
            tweets = list([self.tweets[userId][-10:][::-1]])

        for user in self.following[userId]:
            if user not in self.tweets:
                continue
            tweets.append(self.tweets[user][-10:][::-1])
            
        merged = heapq.merge(*tweets, reverse=True)
        return [tweetId for _, tweetId in islice(merged, 10)]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {followeeId}
        else:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)