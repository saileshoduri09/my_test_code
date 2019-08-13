def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    a= []
    
#     if number in arr  = 0:
    for number in arr:
        if number is 0:
            a
        else:
            if number < 0:
                sum = sum + number
            elif number > 0 :
                count = count + 1
        a = [count,sum]
    
    return a
        
