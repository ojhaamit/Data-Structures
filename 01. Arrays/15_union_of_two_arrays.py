#User function Template for python3
def doUnion(a,n,b,m):
    s = set()

    for i in range(n):
        s.add(a[i])

    for i in range(m):
        s.add(b[i])

    return len(s)
    # if n > m:
    #     for i in range(m):
    #         if b[i] not in a:
    #             a.append(b[i])
    #     return len(a)
        
    # elif m > n:
    #     for i in range(n):
    #         if a[i] not in b:
    #             b.append(a[i])
    #     return len(b)
        
    # else:
    #     for i in range(n):
    #         if a[i] not in b:
    #             b.append(a[i])
    #     return len(b)


#  Driver Code Starts
if __name__=='__main__':
    a = [1, 2, 3, 4, 5]
    n = len(a)
    b = [1, 2, 3]
    m = len(b)

    result = doUnion(a, n, b, m)
    print(result)