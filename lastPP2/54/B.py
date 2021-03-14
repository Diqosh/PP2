import sys, re
pattern = r'[^A-Za-z0-9_]'


if __name__ == "__main__":

    txt = input()
    
    if re.search(pattern, txt):
        print('Not matched!')
    else:
        print('Found a match!')
            

    