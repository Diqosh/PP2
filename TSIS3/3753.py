if __name__ == '__main__':

    num1, num2 = [int(i) for i in input().split()]
    set1 = set()
    for i in range(num1):
        set1.add(int(input()))
    set2 = set()
    for i in range(num2):
        set2.add(int(input()))

    setIntersection = set1.intersection(set2)
    # количество кубики каждого цвета в обоих наборах

    print(len(setIntersection))
    # а затем отсортированные номера цветов в обоих наборах

    for i in sorted(setIntersection):
        print(i, end=' ')
    print('')
    # затем количество  номера оставшие цветов у set1
    print(len(set1 - setIntersection))

    # номера остальных цветов у Ани
    for i in sorted(set1 - setIntersection):
        print(i ,end=' ')
    print('')
    # потом количество\ номера остальных цветов у set2.
    print(len(set2 - setIntersection))

    # отсортированные по возрастанию номера
    for i in sorted(set2 - setIntersection):
        print(i)
