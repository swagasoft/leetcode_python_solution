

def find_subset(nums):
 ans = [[]]
 print('ls ', len)

 for i in range(len(nums) + 1):
    for j in range(i):
        ans.append(nums[j:i])
 return ans

ls = [1,2,3]
print(find_subset(ls))
