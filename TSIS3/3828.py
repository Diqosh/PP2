if __name__ == '__main__':
    text = input().split()
    for index, val in enumerate(text):
        if not (index % 2):
            print(val, end=' ')