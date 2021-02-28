import re

if __name__ == '__main__':
    
    a = int(input())
    for i in range(a):
        word = input()
        print(bool(re.search(r'^[+-]?\d*\.\d+$', word)))
