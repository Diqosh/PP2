import re

patternTime = r'Время: (?P<TIME>.+)'
patternAddress = r'(?P<ADDRESS>г\..+)'
patternBIN = r'БИН (?P<BIN>\d+)'
patternNameOfCompany = r'Филиал (?P<NAMECOMP>.+)'
patternItems = r'\n\d+\.\n(?P<title>.+)\n(?P<COUNT>\d+),\d+.{3}(?P<PRICE>\d+).*\n.*\nСтоимость\n(?P<total>\d+)'

def printNameAndBin(txt):
    print(re.search(patternNameOfCompany, txt).group('NAMECOMP'))
    print(re.search(patternBIN, txt).group('BIN'))
def printTimeAndAddres(txt):
    print(f'Date —— {re.search(patternTime, txt).group("TIME")}')
    print(f'Address —— {re.search(patternAddress, txt).group("ADDRESS")}')


def printItems():
    file = open('raw.txt', encoding='utf8')
    txt = file.read()
    printNameAndBin(txt)
    for i, m in enumerate(re.finditer(patternItems, txt), start=1):
        print(f"{i}.Title ——  {m.group('title')}")
        print(f"\t1.Cout ——  {m.group('COUNT')}")
        print(f"\t2.Unit price ——  {m.group('PRICE')}")
        print(f"\t3.Total price ——  {m.group('total')}")
    file.close()
    printTimeAndAddres(txt)


class Things:
    def __init__(self):
        self.listOfItems = list()
        self.patterns = [(patternNameOfCompany, 'NAMECOMP'), (patternBIN, 'BIN'), (patternAddress, 'ADDRESS'),
                         ('def', 'asd'), (patternTime, 'TIME')]

    def searching(self):
        with open('raw.txt', 'r', encoding="utf8") as rFile:
            for line in rFile:
                for (pattern, name) in self.patterns:
                    if re.search(pattern, line):
                        print(re.search(pattern, line).group(name))
                        self.patterns.remove((pattern, name))


if __name__ == '__main__':
    printItems()
