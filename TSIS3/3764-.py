import sys

def f(elem):
    return elem[1]

if __name__ == '__main__':
    dic = dict()
    text = str()
    for line in sys.stdin:
        text += input() + ' '
    for i in text:
        if i not in dic.keys():
            dic[i] = text.count(i)
    dic_sorted = sorted(dic.items(), key=f, reverse=True)
    for i in dic_sorted:
        print(i[0])
