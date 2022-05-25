def sumNumbers(string):
    sum = 0
    temp = '0'

    for char in string:
        if char.isdigit():
            temp += char
        else:
            # print(temp)
            sum += int(temp)
            temp = '0'

    return sum


if __name__ == "__main__":
    string = 'ab50dt60h4q'
    result = sumNumbers(string)
    print(result)