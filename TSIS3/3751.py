if __name__ == '__main__':
     print(*sorted([int(i) for i in set(input().split()).intersection(set(input().split()))]))

