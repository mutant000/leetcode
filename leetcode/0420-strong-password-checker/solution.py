class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_types = sum(
            (
                not any(character.islower() for character in password),
                not any(character.isupper() for character in password),
                not any(character.isdigit() for character in password),
            )
        )

        repeat_lengths = []
        start = 0

        # 第一步：找出所有长度至少为 3 的连续重复段。
        while start < len(password):
            end = start + 1
            while end < len(password) and password[end] == password[start]:
                end += 1

            repeat_length = end - start
            if repeat_length >= 3:
                repeat_lengths.append(repeat_length)
            start = end

        replacement_count = sum(length // 3 for length in repeat_lengths)
        password_length = len(password)

        if password_length < 6:
            return max(missing_types, 6 - password_length)

        if password_length <= 20:
            return max(missing_types, replacement_count)

        # 第二步：超长时优先删除最能减少替换次数的位置。
        deletion_count = password_length - 20
        remaining_deletions = deletion_count

        one_deletion_groups = sum(
            length % 3 == 0
            for length in repeat_lengths
        )
        used_groups = min(one_deletion_groups, remaining_deletions)
        replacement_count -= used_groups
        remaining_deletions -= used_groups

        two_deletion_groups = sum(
            length % 3 == 1
            for length in repeat_lengths
        )
        used_groups = min(two_deletion_groups, remaining_deletions // 2)
        replacement_count -= used_groups
        remaining_deletions -= used_groups * 2

        replacement_count -= remaining_deletions // 3
        replacement_count = max(0, replacement_count)

        return deletion_count + max(missing_types, replacement_count)
