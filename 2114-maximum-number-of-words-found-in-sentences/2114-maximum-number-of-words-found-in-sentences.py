class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count = 0
        for _ in sentences:
            max_total_words = len(_.split(" "))
            if count == 0:
                count = max_total_words

            elif count >= 1:
                if count < max_total_words:
                    count = max_total_words

        return count
