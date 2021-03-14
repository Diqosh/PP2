
import re

if __name__ == "__main__":
    txt = input()
    pattern = r'(?P<DAY>\d{2}).(?P<MONTH>\d{2}).(?P<YEAR>\d{4})'

    x = re.search(pattern, txt)

    day = int(x.group('DAY'))
    month = int(x.group('MONTH'))
    year = int(x.group('YEAR'))
    
    if 1 <= day <= 31 and 1 <= month <= 12 and  1299 <= year <= 1922:
        print('yes')
    else:
        print('No')
   