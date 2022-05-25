#User function Template for python3

def rotate( arr, n):
    first = arr[0]
    last = arr[-1]
    arr[0] = last
    
    for i in range(1, n):
        arr[i], first = first, arr[i]
    
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    result = rotate(arr, n)
    print(arr)





    
# } Driver Code Ends