class Toupper:
    def __init__(self, a):
        self.a = a
    def print(self):
        if self.a.isupper():
            print(self.a.lower())
        else:
            print(self.a.upper())



if __name__ == '__main__':
    myclass = Toupper(input())
    myclass.print()