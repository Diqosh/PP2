if __name__ == '__main__':
    text = input()
    a = False
    if text[0] == ' ':
        a = True
    print(' ' + ' '.join(text.split())) if a else print(' '.join(text.split()))