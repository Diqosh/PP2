if __name__ == '__main__':
    num = int(input())
    dic = dict()
    for i in range(num):
        st1, st2 = input().split()
        dic[st1] = st2
    textToSynonim = input()
    for m, n in dic.items():
        if textToSynonim == m:
            print(n)
        elif textToSynonim == n:
            print(m)