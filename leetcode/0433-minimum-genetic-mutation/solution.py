from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)

        if endGene not in bank_set:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"

        while queue:
            current, steps = queue.popleft()

            if current == endGene:
                return steps

            for index, original_char in enumerate(current):
                for gene in genes:
                    if gene == original_char:
                        continue

                    mutation = current[:index] + gene + current[index + 1:]

                    if mutation in bank_set and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps + 1))

        return -1
