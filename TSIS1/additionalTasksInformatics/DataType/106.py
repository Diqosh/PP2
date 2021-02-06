class Toupper:
    def __init__(self, a):
        self.a = len(a.split())

    def print(self):
        print(self.a)


if __name__ == '__main__':
    myclass = Toupper(input())
    myclass.print()