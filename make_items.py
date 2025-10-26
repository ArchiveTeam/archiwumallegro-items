import sys

import zstandard

STEP_SIZE = 10 ** 9


def main(start: int, stop: int):
    for i in range(start, stop, STEP_SIZE):
        with zstandard.open('ids_{}-{}.txt.zst'.format(i, i+STEP_SIZE-1), 'w') as f:
            for j in range(i, i+STEP_SIZE, 100):
                f.write('ids:{}-{}\n'.format(j, j+99))

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

