
from typing import List
from unittest import result


def level_operations(ls: List[int]):
    # check for number frequency 
    frequencyDic = {}
    frequency = 0
    total_step = 0

    for item in ls:
         # make a frequency of all item
        if item in frequencyDic:
            frequencyDic[item] = frequencyDic[item] + 1
        else:
            frequencyDic[item] =  1

    for key, value in frequencyDic.items():
        if value  > frequency:
            frequency = key
        
    total_step = num_checker(ls, frequency, total_step, visited = 0, start = True)

     
    return total_step


def num_checker(listNum, target, step, visited, start):

    lenn = len(listNum) 
    while(start):

        for index,  num in enumerate(sorted(listNum)):
        
            if num < target:
                listNum[index] =   num + 1
                step += 1
            if num > target:
                listNum[index] =   num - 1
                step += 1
            if listNum[index] == target:
                visited += 1
            
            
            
        if visited == lenn :
            start = False
            
        num_checker(listNum, target, step, visited, start)
            
    return step
        
    
                
        
        



# list_1 = [1,3,2,2] //2
list_1 = [6,2,8,1]
print('FINAL ', level_operations(list_1))