def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged_intervals = [intervals[0]]
    current_merged_interval = merged_intervals[0]
    i = 1
    while True:
        if i == len(intervals):
            break
        current_checking_interval = intervals[i]
        if (
            current_checking_interval[0] <= current_merged_interval[1] <=
            current_checking_interval[1]
        ):
            current_merged_interval[1] = current_checking_interval[1]
            i += 1
            continue

        if (
            current_merged_interval[0] <= current_checking_interval[0] <=
            current_merged_interval[1] and current_merged_interval[1] >=
            current_checking_interval[1]
        ):
            i += 1
            continue

        merged_intervals.append(current_checking_interval)
        current_merged_interval = current_checking_interval
        i += 1
    return merged_intervals


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


def appearance(intervals: dict[str, list[int]]) -> list[int]:
    timestamps = []
    result = []
    for i in intervals:
        if not is_sorted(intervals[i]):
            list_of_pairs = get_list_of_pairs(intervals[i])
            list_of_pairs = merge_intervals(list_of_pairs)
            list_of_points = []
            for pair in list_of_pairs:
                list_of_points.append(pair[0])
                list_of_points.append(pair[1])
            intervals[i] = list_of_points
        timestamps.extend(intervals[i])
    for timestamp in sorted(list(set(timestamps))):
        if (
            is_include(timestamp, intervals['lesson']) and
            is_include(timestamp, intervals['pupil']) and
            is_include(timestamp, intervals['tutor'])
        ):
            result.append(timestamp)
    return sum(result[i + 1] - result[i] for i in range(0, len(result), 2))


def get_list_of_pairs(points: list[int]) -> list[list[int]]:
    list_of_pairs = []
    i = 0
    while i < len(points):
        list_of_pairs.append([points[i], points[i+1]])
        i += 2
    return list_of_pairs


tests = [
    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                      1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                      1594704512, 1594704513, 1594704564, 1594705150,
                      1594704581, 1594704582, 1594704734, 1594705009,
                      1594705095, 1594705096, 1594705106, 1594706480,
                      1594705158, 1594705773, 1594705849, 1594706480,
                      1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                      1594705149, 1594706463]
        },
        'answer': 3577
    },
    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i},\
        got {test_answer}, expected {test["answer"]}'
