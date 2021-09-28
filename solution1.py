def sockMerchant(n, arr):
    pairs = 0
    i = 0
    arr.sort()
    while (i < (n-1)):
        if (arr[i] == arr[i+1]):
            pairs+=1
            i += 2
        else:
            i+=1
    return pairs
    
    
    
sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
