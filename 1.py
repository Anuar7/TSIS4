import re
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        print(bool(re.match('^[+-]?[0-9]*\.[0-9]+$', input())))