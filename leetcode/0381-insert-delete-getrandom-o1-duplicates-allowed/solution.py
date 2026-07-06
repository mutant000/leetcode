from collections import defaultdict
import random


class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.indices[val].add(len(self.values))
        self.values.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        remove_index = self.indices[val].pop()
        last_value = self.values[-1]

        self.values[remove_index] = last_value
        self.indices[last_value].add(remove_index)
        self.indices[last_value].discard(len(self.values) - 1)

        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
