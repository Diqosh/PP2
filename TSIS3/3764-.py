import sys


def cmp(elem):
    return (-elem[1], elem[0])


if __name__ == '__main__':
    dic = dict()
    text = list()
    for line in sys.stdin:
        text = line.split()
        for i in text:
            dic[i] = dic.get(i, 0) + 1

    sortedItmes = sorted(dic.items(), key=cmp)
    for i in sortedItmes:
        print(i[0])
