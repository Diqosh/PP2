#не закончен
class SearchTwoOtMore:
    def __init__(self, word):
        self.word = word
    def EqualTwo(self, x):
        if x == 2:
            return True
        else:
            return False
    def filtered(self):
        return iterableObj = filter(self.word, EqualTwo())

if __name__ == '__main__':
    a = SearchTwoOtMore(input())
    print(a.filtered())
