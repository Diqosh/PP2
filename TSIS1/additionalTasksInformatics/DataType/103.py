class Toupper:
    def __init__(self, a):
        self.a = a
    def up(self):
        self.a = self.a.upper()
    def print(self):
        print(self.a)

if __name__ == '__main__':
    myclass = Toupper(input())
    myclass.up()
    myclass.print()