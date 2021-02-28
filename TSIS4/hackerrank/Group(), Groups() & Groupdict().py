import re
if __name__ == '__main__':

    a = re.search(r'([a-zA-Z0-9])\1+', input().strip())
    print(a.group(1) if a else -1)