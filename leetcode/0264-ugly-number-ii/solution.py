class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        index_two = 0
        index_three = 0
        index_five = 0

        for index in range(1, n):
            next_two = ugly[index_two] * 2
            next_three = ugly[index_three] * 3
            next_five = ugly[index_five] * 5
            ugly[index] = min(next_two, next_three, next_five)

            if ugly[index] == next_two:
                index_two += 1
            if ugly[index] == next_three:
                index_three += 1
            if ugly[index] == next_five:
                index_five += 1

        return ugly[-1]
