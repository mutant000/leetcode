from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []

        for user in users:
            tweets = self.tweets[user]
            if tweets:
                index = len(tweets) - 1
                time, tweet_id = tweets[index]
                heappush(heap, (-time, tweet_id, user, index - 1))

        feed = []
        while heap and len(feed) < 10:
            _, tweet_id, user, index = heappop(heap)
            feed.append(tweet_id)
            if index >= 0:
                time, next_tweet_id = self.tweets[user][index]
                heappush(heap, (-time, next_tweet_id, user, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
