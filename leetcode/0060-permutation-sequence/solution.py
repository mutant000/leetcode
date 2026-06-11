class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(num) for num in range(1, n + 1)]
        factorial = [1] * (n + 1)

        for num in range(1, n + 1):
            factorial[num] = factorial[num - 1] * num

        k -= 1
        result = []

        for length in range(n, 0, -1):
            block_size = factorial[length - 1]
            index = k // block_size
            k %= block_size
            result.append(numbers.pop(index))

        return "".join(result)
