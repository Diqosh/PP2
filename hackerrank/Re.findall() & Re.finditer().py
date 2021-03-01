import re
if __name__ == '__main__':

    s = input()
    pattern = r'[^AEIOUaeiou](?P<p>[AEIOUaeiou]{2,})[^AEIOUaeiou]'

    for i in re.search(pattern, s):
        print(i.group('p'))
