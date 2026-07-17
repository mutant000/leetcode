class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        block_start = 1
        block_count = 9

        # 第一步：跳过完整的 1 位数、2 位数等数字区间。
        while n > digit_length * block_count:
            n -= digit_length * block_count
            digit_length += 1
            block_start *= 10
            block_count *= 10

        # 第二步：定位区间内的具体数字以及该数字中的具体一位。
        offset = n - 1
        number = block_start + offset // digit_length
        digit_index = offset % digit_length

        return int(str(number)[digit_index])
