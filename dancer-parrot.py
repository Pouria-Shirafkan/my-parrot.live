import os
import time
import random

colors = {
    "1":     "\033[31m",
    "2":   "\033[32m",
    "3":  "\033[33m",
    "4":    "\033[34m",
    "5": "\033[35m",
    "6":    "\033[36m",
    "7":    "\033[37m",
    "8":   "\033[97m"
    }

def main():
    frames = open("1.txt", "r")
    print(colors[str(random.randint(1 ,8))] + frames.read()) 
    time.sleep(0.1)
    os.system('clear')
    frames = open("2.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')
    frames = open("3.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')
    frames = open("4.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read()) 
    time.sleep(0.1)
    os.system('clear')
    frames = open("5.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')
    frames = open("6.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read()) 
    time.sleep(0.1) 
    os.system('clear')
    frames = open("7.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')
    frames = open("8.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')
    frames = open("9.txt", "r")
    print(colors[str(random.randint(1, 8))] + frames.read())  
    time.sleep(0.1)
    os.system('clear')

while True:
    main()
