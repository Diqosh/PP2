#partial
if __name__ == '__main__':
    a = int(input())
    c = int(input())

    _a = a % 100

    if(a // 10 != 0):
        if(a // 100 != 0):
            if (a // 1000 != 0):
                if (a // 10000 == 0):
                    print("YES")


    if a == _a:
        if c == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
#test different