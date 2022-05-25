def longest_substring(string):
    len_str = len(string)

    start = 0
    end = 1

    result = ""

    # while end < len_str:
    #     if string[start] != string[end]:
    #         if string[start] not in result:
    #             result += string[start]
    #     start += 1
    #     end += 1
        
    return result

if __name__ == "__main__":
    input_str = "abcabcbb"
    result = longest_substring(input_str)
    print(result)