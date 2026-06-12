class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        length = max(len(parts1), len(parts2))

        for index in range(length):
            num1 = int(parts1[index]) if index < len(parts1) else 0
            num2 = int(parts2[index]) if index < len(parts2) else 0

            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

        return 0
