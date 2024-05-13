#!/usr/bin/python3
"""Interview question stats module"""


def parse_log_line(line):
    """Parses the info on the standin and give context
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
        (if the format is not this one, the line must be skipped)
        After every 10 lines and/or a keyboard interruption print these statistics from the
        beginning:
        Total file size:
        File size: <total size>
            where <total size> is the sum of all previous <file size>
        Number of lines by status code
            format: <status code>: <number> ascending order
    """
    try:
        _, _, _, _, status_code, file_size = line.split()
        return int(status_code), int(file_size)
    except ValueError:
        return None, None
    
def main():
    """Main entry point"""
    total_size = 0
    status_counts = {}

    try:
        while True:
            line = input()  # Read a line from stdin
            status_code, file_size = parse_log_line(line)
            if status_code is not None:
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            # Print statistics after every 10 lines
            if len(status_counts) % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_counts):
                    print(f"{code}: {status_counts[code]}")
    except KeyboardInterrupt:
        # Handle CTRL + C interruption
        print(f"Total file size: {total_size}")
        for code in sorted(status_counts):
            print(f"{code}: {status_counts[code]}")

if __name__ == "__main__":
    main()