def longestPalindrome(S):
    substrings = []
    max_length = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            substrings.append(S[i:j])

    for i in range(len(substrings)):
        # print(checkPalindrome(substrings[i])[0])
        if checkPalindrome(substrings[i])[0]:
            curr_length = checkPalindrome(substrings[i])[0]
            # print(curr_length)
            if curr_length > max_length:
                max_length = curr_length

    # print(substrings)

    return max_length

def checkPalindrome(str):
    if str == str[::-1]:
        return [len(str), str] 
    return [0, str]

if __name__ == "__main__":
    S = "babad"
    result = longestPalindrome(S)
    print(result)