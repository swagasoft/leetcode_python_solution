def plusMinus(arr):
    # Write your code here
    leen = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    
    for val in arr:
        
        if val  == 0:
            zeros += 1
        elif val > 0 :
            positive += 1
        elif val < 0:
            negative += 1
            
    print("%.6f" % (positive/leen))
    print("%.6f" % (negative/leen))
    print("%.6f" % (zeros/leen))
    