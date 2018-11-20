import csv
import sys
import matplotlib.pyplot as mpl
import configparser


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


x = []
y = []
cp = configparser.ConfigParser()
cp.read('config.ini')

speed = str2bool(cp.get('Graph', 'Speed'))
accuracy = str2bool(cp.get('Graph', 'Accuracy'))

if(speed and accuracy):
    print('Currently both are not supported')
    sys.exit()

with open('data.csv', 'r', newline='') as readFile:
    readCsv = csv.reader(readFile, delimiter=',')
    next(readCsv, None)
    counter = 1
    for row in readCsv:
        if(speed):
            y.append(int(row[0]))  # 0 = Speed | 1 = Accuracy
        else:
            y.append(float(row[1]))  # Accuracy option chosen
        x.append(counter)
        counter += 1

if(speed):
    mpl.plot(x, y, label='Speed')
else:
    mpl.plot(x, y, label='Accuracy')
mpl.legend()
mpl.show()
