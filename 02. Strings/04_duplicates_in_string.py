def duplicatesInString(S):
    char_set = {}

    for i in range(len(S)):
        if S[i] in char_set:
            char_set[S[i]] += 1
        else:
            char_set[S[i]] = 1

    result = []
    for idx, string in enumerate(char_set):
        # print(string, char_set[string])
        if char_set[string] > 1:
            result.append([string, char_set[string]])

    return result


if __name__ == "__main__":
    S = "abba"
    result = duplicatesInString(S)
    print(result)