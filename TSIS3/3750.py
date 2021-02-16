if __name__ == '__main__':
    text1 = set(input().split())
    text2 = set(input().split())
    text3 = text1.intersection(text2)
    print(len(text3))