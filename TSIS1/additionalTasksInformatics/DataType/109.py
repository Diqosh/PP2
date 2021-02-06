# не закончен
if __name__ == '__main__':
    text = input()
    print(*filter(lambda x: text.count(x) >= 2, set(text)))
    