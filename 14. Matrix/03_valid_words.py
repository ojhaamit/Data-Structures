def isValidWords(words):

    for i, row in enumerate(words):
        col_word = ''.join([row_word[i] for row_word in words if i < len(row_word)])
        if len(col_word) != len(row) or col_word != row:
            return False

    return True

if __name__ == "__main__":
    words = ["ball","area","read","lady"]
    result = isValidWords(words)
    print(result)