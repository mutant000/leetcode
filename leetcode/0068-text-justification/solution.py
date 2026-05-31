from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        index = 0

        while index < len(words):
            line_words = []
            line_letters = 0

            while index < len(words):
                next_length = line_letters + len(words[index]) + len(line_words)
                if next_length > maxWidth:
                    break

                line_words.append(words[index])
                line_letters += len(words[index])
                index += 1

            is_last_line = index == len(words)
            result.append(self.build_line(line_words, line_letters, maxWidth, is_last_line))

        return result

    def build_line(
        self, words: List[str], letters: int, max_width: int, is_last_line: bool
    ) -> str:
        if len(words) == 1 or is_last_line:
            line = " ".join(words)
            return line + " " * (max_width - len(line))

        gaps = len(words) - 1
        total_spaces = max_width - letters
        base_spaces, extra_spaces = divmod(total_spaces, gaps)
        parts = []

        for index, word in enumerate(words[:-1]):
            spaces = base_spaces + (1 if index < extra_spaces else 0)
            parts.append(word + " " * spaces)

        parts.append(words[-1])
        return "".join(parts)
