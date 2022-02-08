

class Solution:

    def medianSlidingWindow( nums: list, k: int):
        window = []
        result = []
        

        for i, num in enumerate(nums):
            window.append(num)
            if len(window) == k:
                if len(window) == k:
                    sortW = sorted(window)
                    lennn =  len(window)
                    if lennn % 2 == 1:
                        result.append(sortW[lennn //2])
                        del  window[0]
                    else:
                        result.append((sortW[lennn //2] +  sortW[lennn //2- 1])/ 2)
                        del window[0]

            else:
                pass

        return result




# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
nums = [1,4,2,3]
k = 4
print(Solution.medianSlidingWindow(nums, k))
