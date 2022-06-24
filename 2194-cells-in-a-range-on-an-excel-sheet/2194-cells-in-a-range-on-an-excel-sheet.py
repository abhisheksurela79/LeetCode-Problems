class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        import re

        x = []

        data = [[_[0], (re.findall("[0-9]+", _))[0]] for _ in s.split(":")]

        row_one = ord(data[0][0])
        row_two = ord(data[1][0])

        column_first = int(data[0][1])
        column_second = int(data[1][1])

        for _ in range(row_one, (row_two + 1)):
            for j in range(column_first, (column_second + 1)):
                x.append(f"{chr(_)}{j}")

        return x
        