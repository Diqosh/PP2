class CheckIsPol:
    def __init__(self, a):
        self.a = a
        self.b = a[::-1]
    def check(self):
        print('yes') if self.a == self.b else print('no')

if __name__ == '__main__':
    MyClass = CheckIsPol(input())
    MyClass.check()
