import sys

with open('input/2.txt') as f:
    data = [[int(y) for y in x.strip('\n').split(' ')] for x in f.readlines()]    

def check_safe(report: list, inc: bool) -> dict:
    i = 0
    while i < len(report) - 1:
        if inc:
            if report[i] > report[i + 1]:
                return {
                    'status': 'error',
                    'reason': 'dec',
                    'idx': i,
                }

            if not 0 < abs(report[i] - report[i + 1]) <= 3:
                return {
                    'status': 'error',
                    'reason': 'diff',
                    'idx': i,
                    'diff': abs(report[i] - report[i + 1])
                }
        if not inc:
            if report[i] < report[i + 1]:
                return {
                    'status': 'error',
                    'reason': 'inc',
                    'idx': i,
                }

            if not 0 < abs(report[i] - report[i + 1]) <= 3:
                return {
                    'status': 'error',
                    'reason': 'diff',
                    'idx': i,
                    'diff': abs(report[i] - report[i + 1])
                }
        i += 1
    return {
        'status': 'success'
    }

safe = 0
count = 0
for report in data:
    increasing = False
    is_safe = True
    if report[0] < report[len(report)-1]: increasing = True

    check = check_safe(report, increasing)
    if check['status'] == 'success':
        safe += 1

    if check['status'] == 'error':
        j = 0
        while j < len(report):
            if j == 0:
                 nreport = report[1:]
            else:
                nreport = report[:j] + report[j+1 :]
            ncheck = check_safe(nreport, increasing)

            if ncheck['status'] == 'success':
                safe += 1
                break
            j += 1
        
print(f'{safe=}')
