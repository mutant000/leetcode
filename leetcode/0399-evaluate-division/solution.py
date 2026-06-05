from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend].append((divisor, value))
            graph[divisor].append((dividend, 1 / value))

        def evaluate(start: str, target: str) -> float:
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                variable, product = queue.popleft()

                if variable == target:
                    return product

                for neighbor, ratio in graph[variable]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * ratio))

            return -1.0

        return [evaluate(start, target) for start, target in queries]
