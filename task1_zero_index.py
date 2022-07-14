def task(array: str) -> int:
    ctr = 0
    for i in array:
        if i != '0':
            ctr += 1
        else:
            return ctr


assert task('11110000') == 4
assert task('111111111111111111111111100000000') == 25
assert task('111111111110000000000000000') == 11
assert task('10') == 1
