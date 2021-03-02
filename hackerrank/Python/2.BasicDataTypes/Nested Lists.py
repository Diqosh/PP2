def deleteMinElem(records):
    min1 = min([x for [_, x] in records])
    i = len(records) - 1;
    while i >= 0:
        if records[i][1] == min1:
            records.remove(records[i])
        i = i - 1



if __name__ == '__main__':
    a = int(input())
    records = list()
    for i in range(a):
        name = input()
        score = float(input())
        records.append([name, score])
    deleteMinElem(records)
    min2 = min([x for [z, x] in records])

    recordsSecondLowest = [y for [y, x] in records if x == min2]
    recordsSecondLowest.sort()
    for x in recordsSecondLowest:
        print(x)

