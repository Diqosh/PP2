import re

patternTime = r'^Время: (?P<TIME>.+)'
patternAddress = r'(?P<ADDRESS>^г\..+)'
patternBIN = r'^БИН (?P<BIN>\d+)'
patternNameOfCompany = r'^Филиал (?P<NAMECOMP>.+)'
patternItems = r'\d+\.\n(&P<TITLE>.+)\n(?P<COUNT>\d+).*\n(^P<PRICE>\d+).*\nСтоимость\n(?P<total>\d+).*'






class Things:
    def __init__(self):
        self.listOfItems = list()
        self.patterns = [(patternNameOfCompany, 'NAMECOMP'), (patternAddress, 'ADDRESS'), (patternBIN, 'BIN'), (patternTime, 'TIME' )]


    def searching(self):
        with open('raw.txt', 'r', encoding="utf8") as rFile:
            for line in rFile:
                for (pattern, name) in self.patterns:
                    if re.search(pattern, line):
                        print(re.search(pattern, line).group(name))
                        self.patterns.remove((pattern, name))






if __name__ == '__main__':
    myClass = Things()
    myClass.searching()
#незакончен







