#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo
"""
    Docstring:
"""


def search_word(pattern=r"Ben", file=r"/Users/blb882/Documents/PycharmProjects/supertechV1/words"):
    lines_matched = 0
    with (open(file, mode="rt") as fh_in):
        for (line_num, line) in enumerate(fh_in, start=1):
            if line.isascii() and pattern in line:
                print(line_num, line, end="")
                lines_matched += 1
    return lines_matched

total_lines = 0
total_lines += search_word("done", r"/Users/blb882/Documents/PycharmProjects/supertechV1/words")
print("-" * 50)
total_lines += search_word("Ben", r"/Users/blb882/Documents/PycharmProjects/supertechV1/words")

print(f"total lines matched: {total_lines}")