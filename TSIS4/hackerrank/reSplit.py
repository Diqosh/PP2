import re

if __name__ == '__main__':
    word = input()
    for i in re.split('[.,]', word):
        print(i)
