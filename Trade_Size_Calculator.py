from datetime import datetime
import sys
import os

def tsc1():
    print('Welcome to the Trade Size Calculator! What is your risk profile?')
    print('Type c for conservative, b for balanced, and a for aggressive.')
    tsl1 = input()
    if tsl1 == 'c':
        print('What is your account balance?')
        ab1 = float(input())
        print('What is your available margin?')
        am1 = float(input())
        print('How much leverage do you have? If 50:1, put 50. If 1:1, put 1.')
        l1 = float(input())
        print('Your Trade size should be')
        print((l1 * (ab1 - (ab1 - am1))) / 20)
    
    elif tsl1 == 'b':
        print('What is your account balance?')
        ab2 = float(input())
        print('What is your available margin?')
        am2 = float(input())
        print('How much leverage do you have? If 50:1, put 50. If 1:1, put 1.')
        l2 = float(input())
        print('Your Trade size should be')
        print((l2 * (ab2 - (ab2 - am2))) / 10)
    elif tsl1 == 'a':
        print('What is your account balance?')
        ab3 = float(input())
        print('What is your available margin?')
        am3 = float(input())
        print('How much leverage do you have? If 50:1, put 50. If 1:1, put 1.')
        l3 = float(input())
        print('Your Trade size should be')
        print((l3 * (ab3 - (ab3 - am3))) / 5)
    else:
        print('Invalid Input, Try again')

while True:
    tsc1()
    while True:
        exit = str(input("Do you want to calculate this again? y/n?"))
        if exit in ('y', 'n'):
            break
        print('Invalid Input, try again.')
        if exit == 'y':
            tsc1()
        else:
            print('Thank you for using the calculator! Goodbye!')
            break