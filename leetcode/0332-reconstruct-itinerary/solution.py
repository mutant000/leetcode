from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)

        route = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
