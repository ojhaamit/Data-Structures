def reverse_array(array):
    print(array)
    if len(array) == 0:
        return
    
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    # print("hello")
    # print(array)

    return array

if __name__ == "__main__":
    original_array = [4, 1, 2, 8, 9]
    # print("hi")
    result = reverse_array(original_array)
    print(result)


#Time Complexity: O(n)
#Space Complexity: O(1)