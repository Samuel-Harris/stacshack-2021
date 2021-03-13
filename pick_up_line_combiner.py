import csv
import os
from itertools import chain
from glob import glob


def main():
    output = ''
    for file_name in (chain.from_iterable(glob(os.path.join(x[0], '*.csv')) for x in os.walk('data'))):
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            output += '\n'.join(list(reader)[0])

    with open('data.txt', 'w') as f:
        f.write(output)


if __name__ == main():
    main()
