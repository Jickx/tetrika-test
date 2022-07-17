def merge_intervals(intervals: list[int]) -> list[int]:
    result = []
    timestamps = sorted(list(set(intervals)))
    intervals = [[intervals[i], intervals[i + 1]] for i
                 in range(0, len(intervals), 2) if
                 (intervals[i + 1] - intervals[i]) > 0]
    for timestamp in timestamps:
        ctr = 0
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if start <= timestamp <= end:
                ctr += 1
            if ctr > 1:
                break
        if ctr == 1:
            result.append(timestamp)
    return result


def is_sorted(intervals) -> bool:
    for i, el in enumerate(intervals[1:]):
        if el < intervals[i]:
            return False
    return True


def is_include(timestamp: list[int], intervals: list[int]) -> bool:
    for i in range(0, len(intervals), 2):
        start = intervals[i]
        end = intervals[i + 1]
        if start <= timestamp <= end:
            return True
        elif timestamp < start:
            return False


def appearance(intervals: list[int]) -> int:
    data = intervals[2]['data']
    timestamps = []
    result = []
    for i in data:
        if not is_sorted(data[i]):
            data[i] = merge_intervals(data[i])
        else:
            timestamps.extend(data[i])
    for timestamp in sorted(list(set(timestamps))):
        if is_include(timestamp, data['lesson']) and\
           is_include(timestamp, data['pupil']) and\
           is_include(timestamp, data['tutor']):
            result.append(timestamp)
    print(sum(result[i + 1] - result[i] for i in range(0, len(result), 2)))
        
    return result, len(result)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117},
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                        1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009,
                        1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480,
                        1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463]},
     'answer': 3577},
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565},
]


# tests = [
#     {'data': {'lesson': [1, 100],
#               'pupil': [30, 90, 10, 20,
#                         40, 50],
#               'tutor': [20, 51, 51, 51, 60, 90]},
#      'answer': 3117},
# ]


print(appearance(tests))


# if __name__ == '__main__':
#     for i, test in enumerate(tests):
#         test_answer = appearance(test['data'])
#         assert test_answer == test['answer'], f'Error on test case {i},\
#         got {test_answer}, expected {test["answer"]}'
