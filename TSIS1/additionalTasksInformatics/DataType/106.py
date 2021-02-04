class Toupper:
    def __init__(self, a):
        self.a = max(a.split(), key=lambda x: len(x))

    def printMax(self):
        print(self.a, len(self.a), sep = '\n')


if __name__ == '__main__':
    myclass = Toupper(input())
    myclass.printMax()
