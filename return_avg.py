def find_average(arr):
    if len(arr) == 0:
        return 0 
    else:
        # count = num of elements in arr 
        count = len(arr) 
        # total is sum of elements 
        for i in arr:
            total += i
        # avg = count / total 
        avg = total/count
        
        return avg