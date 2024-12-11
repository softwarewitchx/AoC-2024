
def count_safe_reports(input_file_path):
    reports = []
    unsafe_reports = 0

    with open(input_file_path, 'r') as io:
        text = io.read().strip().split('\n')

        for row in text:
            report = row.split(' ')
            reports.append(report)

        for report in reports:
            increasing = None

            for i in range(0, len(report) - 1):
                level, next_level = int(report[i]), int(report[i + 1])
                distance = abs(level - next_level)

                if (distance >= 1 and distance <= 3):

                    if (level > next_level):

                        if (increasing == True):
                            unsafe_reports += 1
                            break

                        increasing = False

                    elif (level < next_level):

                        if (increasing == False):
                            unsafe_reports += 1
                            break

                        increasing = True

                else:
                    unsafe_reports += 1
                    break

        safe_reports = len(reports) - unsafe_reports
        return safe_reports

safe_reports = count_safe_reports('./puzzle-input.txt')
print(safe_reports)
