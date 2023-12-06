#!/usr/bin/python3
"""stats module"""
import sys


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for i, line in enumerate(sys.stdin, 1):
            tokens = line.split()
            if len(tokens) >= 9:
                status_code = int(tokens[-2])
                file_size = int(tokens[-1])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (CTRL+C)
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
