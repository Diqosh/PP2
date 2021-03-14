if __name__ == "__main__":
    a = int(input())
    x = sorted(set(map(int, input().split())))
    
    for index, value in enumerate(x, start=1):
        print(f'{index} {value}')
