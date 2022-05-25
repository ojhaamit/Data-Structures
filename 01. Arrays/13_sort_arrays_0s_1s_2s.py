def sort012(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            count_0 += 1
        elif arr[i] == 1:
            count_1 += 1
        else:
            count_2 += 1
            
    for i in range(len(arr)):
        if count_0 !=0:
            count_0 -= 1
            arr[i] = 0
            
        elif count_1 !=0:
            count_1 -= 1
            arr[i] = 1
            
        elif count_2 !=0:
            count_2 -= 1
            arr[i] = 2
            
    return arr


#  Driver Code Starts

if __name__ == '__main__':
    arr = [0, 1, 0, 1, 2, 0, 1]
    result = sort012(arr)
    print(result)
