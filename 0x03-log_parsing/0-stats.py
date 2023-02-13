import sys

# Keep track of the total file size

total_size = 0

# Keep track of the number of lines for each status code

status_code_counts = {}

# Read from stdin line by line

for line in sys.stdin:

    try:

        # Parse the line

        parts = line.split()

        ip_address = parts[0]

        date = parts[2].strip("[").strip("]")

        request = parts[3].strip("\"")

        status_code = int(parts[4])

        file_size = int(parts[5])

        # Update the total file size

        total_size += file_size

        # Update the count for this status code

        if status_code in status_code_counts:

            status_code_counts[status_code] += 1

        else:

            status_code_counts[status_code] = 1

    except:

        # If the line is not in the correct format, skip it

        continue

    # Check if 10 lines have been processed or if the script was interrupted

    if (sys.stdin.readline() == '') or (len(status_code_counts) % 10 == 0):

        # Print the total file size

        print("File size:", total_size)

        # Print the number of lines for each status code

        for status_code in sorted(status_code_counts.keys()):

            print("{}: {}".format(status_code, status_code_counts[status_code]))

