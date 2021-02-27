import re, sys

for a in sys.stdin:
    print(bool(re.search(r'[+-]?\d*\.\d+$', a)))