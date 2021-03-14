if __name__ == "__main__":
    a = input()
    set1 = set(input().split())
    b = input()
    set2 = set(input().split())

    print(set1 - set2)
    print(set2 - set1)