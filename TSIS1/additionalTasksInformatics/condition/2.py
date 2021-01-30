if __name__ == '__main__':
    a = int(input())
    if a % 400 == 0:
        print("YES")
        exit()

    if a % 100 == 0:
        print("NO")
        exit()

    if a % 4 == 0:
        print("YES")
    else:
        print("NO")