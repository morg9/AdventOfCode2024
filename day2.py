def safeReport(report):
    levels = list(map(int, report.split()))

    is_ascending = all(levels[i] < levels[i+1] for i in range(len(levels)-1))
    is_descending = all(levels[i] > levels[i+1] for i in range(len(levels)-1))
    valid_difference = all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels)-1))

    return (is_ascending or is_descending) and valid_difference

def count_safeReport():
    with open('input/daytwoinput.txt') as f:
        return sum(1 for line in f if safeReport(line.strip()))

count = count_safeReport()
print(f"The number of safe reports is {count_safeReport()}")