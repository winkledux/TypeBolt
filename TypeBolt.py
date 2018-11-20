import time
import sys
import os.path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import configparser
from configparser import Error
import csv


def str2Int(str):
    parsedList = str.split()
    return int(parsedList[0])


def str2Float(str):
    parsedList = str.split()
    return float(parsedList[0])


config = configparser.ConfigParser()
tipoBrowser = None
driverLocation = None
try:
    config.read('config.ini')
    tipoBrowser = config.get('User', 'Browser').lower()
    if(tipoBrowser != 'chrome' and tipoBrowser != 'firefox'):
        print('Browser not supported!')
        sys.exit()
    if(tipoBrowser == 'firefox'):
        driverLocation = config.get('Driver', 'geckodriver')
    elif(tipoBrowser == 'chrome'):
        driverLocation = config.get('Driver', 'chromedriver')
except Error:
    print('Config file is damaged/missing :(')
    sys.exit()

if(not os.path.isfile('data.csv')):
    with open('data.csv', 'w', newline='') as createFile:
        x = csv.writer(createFile, delimiter=',')
        x.writerows([['Speed', 'Accuracy']])

url = 'https://www.typingbolt.com'
typeBolt = None
try:
    if(tipoBrowser == 'firefox'):
        typeBolt = webdriver.Firefox(executable_path=driverLocation)
    elif(tipoBrowser == 'chrome'):
        typeBolt = webdriver.Chrome(executable_path=driverLocation)
except WebDriverException:
    print('Missing web driver. ', end='')
    print('Try installing chromedriver(chrome) or geckodriver(firefox)')
    sys.exit()

typeBolt.get(url)
typeBolt.maximize_window()  # Maximize window
accuracy = typeBolt.find_element_by_id('accuracy')
speed = typeBolt.find_element_by_id('speed')
numAccuracy = str2Float(accuracy.text)
numSpeed = str2Int(speed.text)


while True:
    accuracyText = accuracy.text
    speedText = speed.text
    tmpAccuracy = str2Float(accuracyText)
    tmpSpeed = str2Int(speedText)
    if(tmpAccuracy != numAccuracy or tmpSpeed != numSpeed):
        numAccuracy = tmpAccuracy
        numSpeed = tmpSpeed
        with open('data.csv', 'a', newline='') as updateFile:
            csvFile = csv.writer(updateFile, delimiter=',')
            csvFile.writerow([numSpeed, numAccuracy])
    time.sleep(4)  # Decrease this to check more frequently
