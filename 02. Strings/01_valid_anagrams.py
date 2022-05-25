def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_set = {}

    for i in range(len(str1)):
        if str1[i] in char_set:
            char_set[str1[i]] += 1
        else:
            char_set[str1[i]] = 1

    for i in range(len(str2)):
        if str2[i] not in char_set:
            return False
        else:
            char_set[str2[i]] -= 1

    return True
        
        

if __name__ == "__main__":
    str1 = "anagram"
    str2 = "nagaram"

    result = anagrams(str1, str2)
    print(result)