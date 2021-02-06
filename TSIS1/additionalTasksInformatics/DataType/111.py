import sys
if __name__ == '__main__':
    x = 0
    y = 0
    for line in sys.stdin:
        directon, num = line.split()
        num = int(num)
        if directon == "North":
            y += num
        elif directon == "South":
            y -= num
        elif directon == "East":
            x += num
        elif directon == "West":
            x -= num
    print(x, y)