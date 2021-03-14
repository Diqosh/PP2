import csv

if __name__ == '__main__':
    wfile = open(r'D:\kbtu\2\pp2\PP2\quiz1\2\w.csv', 'a')
    txts = list()

    with open(r'D:\kbtu\2\pp2\PP2\quiz1\2\r.csv', 'r') as rfile:
        for line in rfile:
            txts.append(line.strip())

    i = 0


    while True:
        if i + 1 == len(txts):
            
            break

        if len(txts[i]) > len(txts[i+1]):

            wfile.write('yes\n')

        else:

            wfile.write('no\n')

        i += 1
        
    
    
        
        
        



