import sys
import csv
if len(sys.argv) != 3:
    sys.exit("too many or too few arguments try again")
else:
    original = sys.argv[1]
    output = sys.argv[2]

try:
    with open(original, 'r') as csvfile:
        myreader = csv.DictReader(csvfile)
        with open(output, 'w', newline="") as csvfile:
            fieldnames = ['first', 'last', 'House']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in myreader:
                first_name, last_name = row['NAME'].split(maxsplit=1)
                writer.writerow({'first': first_name, 'last': last_name, 'House': row['HOUSE']})

except FileNotFoundError:
    sys.exit("your file cannot be found in this directory")

except ValueError:
    sys.exit("error try again")
