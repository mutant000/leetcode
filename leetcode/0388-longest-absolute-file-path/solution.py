class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path_length_by_depth = {0: 0}
        longest_path_length = 0

        for entry in input.split("\n"):
            depth = len(entry) - len(entry.lstrip("\t"))
            name = entry[depth:]
            current_path_length = path_length_by_depth[depth] + len(name)

            if "." in name:
                longest_path_length = max(longest_path_length, current_path_length)
            else:
                path_length_by_depth[depth + 1] = current_path_length + 1

        return longest_path_length
