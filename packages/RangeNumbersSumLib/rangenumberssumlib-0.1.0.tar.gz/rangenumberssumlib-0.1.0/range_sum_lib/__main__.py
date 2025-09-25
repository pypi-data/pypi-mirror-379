import sys
from . import range_sum

def main():
    if len(sys.argv) != 3:
        print('Usage: rangesumlibsn a b')
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(range_sum(a, b))

if __name__ == '__main__':
    main()
