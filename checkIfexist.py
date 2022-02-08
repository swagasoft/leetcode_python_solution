class Solution(object):
    def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        for i in range(len(arr)):

            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:
                    return True

        return False

    arr = [7, 1, 14, 11]
    print(checkIfExist(arr))
