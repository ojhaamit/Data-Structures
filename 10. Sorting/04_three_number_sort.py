def threeNumberSort(array, order):
    # Write your code here.
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    for i in range(len(array)):
        if array[i] == order[0]:
            count_1 += 1
        elif array[i] == order[1]:
            count_2 += 1
        else:
            count_3 += 1
    
    for i in range(len(array)):
        if count_1 != 0:
            array[i] = order[0]
            count_1 -= 1
        elif count_2 != 0:
            array[i] = order[1]
            count_2 -= 1
        elif count_3 != 0:
            array[i] = order[2]
            count_3 -= 1
    
    return array

if __name__ == "__main__":
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    result = threeNumberSort(array, order)
    print(result)
	
	
