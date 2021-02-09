if __name__ == '__main__':
    addressList = input().split('.')
    for i in addressList:
        try:
            i = int(i)
            if 0 <= i <= 255:
                continue
            else:
                print('0')
                quit()
        except:
            print('0')
            quit()
    else:
        print('1')