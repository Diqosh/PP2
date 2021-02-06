class CheckPol:
    def __init__(self, word):
        self.word = word
    def check(self):
        return True if self.word == self.word[::-1] else False

if __name__ == '__main__':
    text = ''.join(input().split())
    MyClass = CheckPol(text)
    print("yes") if MyClass.check() else print("no")
