from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 第一步：身高从高到低排列，同身高按 k 从小到大排列。
        ordered_people = sorted(
            people,
            key=lambda person: (-person[0], person[1]),
        )

        # 第二步：高个子的位置已确定，直接按 k 插入当前人。
        reconstructed_queue = []
        for person in ordered_people:
            reconstructed_queue.insert(person[1], person)

        return reconstructed_queue
