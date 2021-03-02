if __name__ == '__main__':
    N = int(input())
    ls = list()
    mainLs = list()
    for _ in range(N):
        txt = input().split()
        ls.append(txt)
    for i in ls:
        if i[0] == 'insert':
            mainLs.insert(int(i[1]) , int(i[2]))
        elif i[0] == 'print':
            print(mainLs)
        elif i[0] == 'remove':
            mainLs.remove(int(i[1]))
        elif i[0] == 'append':
            mainLs.append(int(i[1]))
        elif i[0] == 'sort':
            mainLs.sort()
        elif i[0] == 'pop':
            mainLs.pop()
        elif i[0] == 'reverse':
            mainLs.reverse()