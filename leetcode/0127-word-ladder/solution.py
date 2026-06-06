from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_length = len(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for index in range(word_length):
                pattern = word[:index] + "*" + word[index + 1:]
                patterns[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for index in range(word_length):
                pattern = word[:index] + "*" + word[index + 1:]

                for next_word in patterns[pattern]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))

                patterns[pattern] = []

        return 0
