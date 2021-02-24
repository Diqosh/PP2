import re

if __name__ == '__main__':

    with open('raw.txt', 'r', encoding='UTF8') as file:
        for line in file:
            line = line.rstrip()
            pattern = re.search(r".+БИН[. ]*(?P<BIN>\d+).+НДС[. ]*(?P<NDS>\d+)", line)

            x = re.compile(pattern)
            for match in x.finditer(line):