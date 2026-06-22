def most_frequent_item_count(array): 
    if array == []:
        return 0
    else:
        count = {}
        for i in array:
            if i in count:
                count[i] += 1
            else:
                count[i] = 0
                count[i] +=1
        return max(count.values())