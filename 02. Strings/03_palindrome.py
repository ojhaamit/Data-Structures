def isPalindrome(S):
    start = 0
    end = len(S) - 1
    
    while start < end:
        if S[start] == S[end]:
            start += 1
            end -= 1
        else:
            return 0
    return 1

if __name__ == "__main__":
    S = "abba"
    result = isPalindrome(S)
    print(result)