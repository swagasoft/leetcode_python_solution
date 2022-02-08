# pylint: disable=unsupported-assignment-operation
class Solution:

    def reverseString(s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(ls: list, start, end):
            ls[start], ls[end] = ls[end], ls[start]

        end = len(s) - 1
        start = 0
        while start <= end:
            swap(s, start, end)
            start += 1
            end -= 1

    nums = ["h", "e", "l", "l", "o"]
    reverseString(nums)
