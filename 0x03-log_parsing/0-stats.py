#!/usr/bin/python3
'''parsing log data content'''
import re
import signal
import sys
from typing import List, Tuple


def print_list(logs: List[Tuple[int, int]], filesizes: List[int]) -> None:
    '''
        print the value of a list in this format
        <status code>: <number>
    '''
    totalsize = sum(filesizes)
    sorted(logs)
    print(f'File size: {totalsize}')
    for key in sorted(logs):
        print(f"{key}: {logs[key]}")


def main():
    '''start of execution where the log data will be parsed'''

    format_pattern = r'(\d{1,3}\.?){3}\d{1,3} - \[\d{4,}(-\d{1,2}){2} '\
        r'(\d{1,2}:){2}\d{1,2}.\d{1,8}\] "GET /projects/260 HTTP/1.1" (\d{3}'\
        r') (\d{1,4})'
    result = {}
    sizes = []

    try:
        count = 0
        for line in sys.stdin:
            match = re.match(format_pattern, line)
            if not match:
                continue
            result[match.group(4)] = result.get(match.group(4), 0) + 1
            sizes.append(int(match.group(5)))
            count += 1

            if count % 10 == 0:
                print_list(result, sizes)

        print_list(result, sizes)
    except KeyboardInterrupt:
        print_list(result, sizes)
        sys.exit(0)


if __name__ == "__main__":
    main()
