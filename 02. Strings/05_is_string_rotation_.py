def isRotations(A1, B1):
    char_set = {}

    for char in A1:
        if char in char_set:
            char_set[char] += 1
        else:
            char_set[char] = 1

    for char in B1:
        if char in char_set:
            char_set[char] -= 1
    
    for i in char_set:
        # print(i)
        if char_set[i] != 0:
            return False

    return True

if __name__ == "__main__":
    A1 = "ABACD"
    B1 = "CDABA"
    result = isRotations(A1, B1)
    print(result)