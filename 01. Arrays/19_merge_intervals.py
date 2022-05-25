def mergeIntervals(intervals):
    intervals.sort(key = lambda i : i[0])
    outputs = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = outputs[-1][1]
        if last_end >= start:
            outputs[-1][1] = max(last_end, end)
        else:
            outputs.append([start, end])

    return outputs


if __name__ == "__main__":
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = mergeIntervals(nums)
    print(result)