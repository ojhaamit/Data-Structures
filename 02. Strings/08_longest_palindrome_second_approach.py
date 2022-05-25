def longestPalindrome(S):
    result = ""
    max_length = 0

    for i in range(len(S)):
        #odd palindrome
        l, r = i, i
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if (r - l + 1) > max_length:
                # print((r - 1 + 1), S[l:r+1])
                result = S[l:r+1]
                max_length = r - l + 1
            l -= 1
            r += 1

        #even palindrome
        l, r = i, i + 1
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if (r - l + 1) > max_length:
                # print(S[l:r+1])
                result = S[l:r+1]
                max_length = r - l + 1
            l -= 1
            r += 1
    
    return result

if __name__ == "__main__":
    S = "abaxyzzyxf"
    result = longestPalindrome(S)
    print(result)
