

ls = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]

k = max(ls)
count_list = [0] * (k+ 1)
print( count_list)
print(len(count_list))

for i in range(0, len(ls)):
    count_list[ls[i]] += 1
    
print(count_list)
for j in range(1, len(count_list)):
    count_list[j] = count_list[j] + count_list[j-1]
    
print(count_list)
new_lss = [0] * len(ls)

for i in range(len(ls) - 1,0,-1):
    ele = ls[i]
    print('ele ', ele)
    val = count_list[ele]
    new_val = (val - 1)
    count_list[ele] = new_val

    new_lss[new_val] = ele
print('result ', new_lss)
    
    
    
# print(ls)