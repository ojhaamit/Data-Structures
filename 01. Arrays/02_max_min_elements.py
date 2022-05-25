class Pair():
    def __init__(self):
        self.min = 0
        self.max = 0

def return_min_max(array, len_array):
    minmax = Pair()

    if len_array == 1:
        minmax.min = array[0]
        minmax.max = array[0]
        return minmax

    if array[0] > array[1]:
        minmax.max = array[0]
        minmax.min = array[1]
    else:
        minmax.max = array[1]
        minmax.min = array[0]

    for i in range(2, len_array):
        if array[i] > minmax.max:
            minmax.max = array[i]
        elif array[i] < minmax.min:
            minmax.min = array[i]

    return minmax

if __name__ == "__main__":
    array = [1000, 11, 445, 1, 330, 3000]
    len_array = len(array)
    result = return_min_max(array, len_array)
    print(result.min, result.max)

#Time Complexity: O(n)
#Space Complexity: O(1)