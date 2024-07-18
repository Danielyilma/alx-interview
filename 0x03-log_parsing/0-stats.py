#!/usr/bin/python3
'''parsing log data content'''
import re
import signal
from typing import List, Tuple


result = [] 


def print_list(logs: List[Tuple[int, int]]) -> None:
    '''
        print the value of a list in this format
        <status code>: <number>
    '''
    sum = 0
    for log in logs:
        sum += int(log[1])
    print(f'File size: {sum}')
    for log in logs:
        print(f"{log[0]}: {log[1]}")


def main():
    '''start of execution where the log data will be parsed'''

    format_pattern = '(\d{1,3}\.?){3}\d{1,3} - \[\d{4,}(-\d{1,2}){2} \
(\d{1,2}:){2}\d{1,2}.\d{1,8}\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d{1,4})'
    try:
        while True:
            result = []
            for i in range(10):
                line = input()
                match = re.match(format_pattern, line)
                if not match:
                    continue

                result.append((match.group(4), match.group(5)))

            result.sort(key=lambda x: x[0])
            print_list(result)
    except KeyboardInterrupt:
        result.sort(key=lambda x: x[0])
        print_list(result)
        main()


if __name__ == "__main__":
    main()
