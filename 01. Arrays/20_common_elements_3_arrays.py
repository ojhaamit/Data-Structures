#User function Template for python3
def commonElements (A, B, C, n1, n2, n3):
    # your code here
    set_a = set()
    for i in range(n1):
        set_a.add(A[i])
    
    intersection_ab = set()
    for i in range(n2):
        if B[i] in set_a:
            intersection_ab.add(B[i])
            
    intersection_abc = set()
    for i in range(n3):
        if C[i] in intersection_ab:
            intersection_abc.add(C[i])
        
    # print(intersection_abc)   
    result = []
    for i in intersection_abc:
        result.append(i)
        
    result.sort()
        
    return result
        # return intersection_abc


#  Driver Code Starts

if __name__ == "__main__":
    A = [1, 5, 10, 20, 40, 80]
    n1 = len(A)
    B = [6, 7, 20, 80, 100]
    n2 = len(B)
    C = [3, 4, 15, 20, 30, 70, 80, 120]
    n3 = len(C)
    result = commonElements(A, B, C, n1, n2, n3)
    print(result)
