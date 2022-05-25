def reverseString(string):
    start = 0
    end = len(string) - 1

    while start < end:
        swap(start, end , string)
        start += 1
        end -= 1

    return string

def swap(start, end, string):
    string[start], string[end] = string[end], string[start]


if __name__ == "__main__":
    string = ["h","e","l","l","o"]
    result = reverseString(string)
    print(result)