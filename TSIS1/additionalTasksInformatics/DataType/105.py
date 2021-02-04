class Toupper:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print(self):
        print("yes") if self.a == self.b else print("no")


if __name__ == '__main__':
    myclass = Toupper(input(),input())
    myclass.print()