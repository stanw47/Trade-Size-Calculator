import sys

def tsl():
    print('Welcome to the Trade Size Calculator! What is your risk profile? type c for conservative, b for balanced, and a for aggressive.')
    tsl == input()
    print('What is your account balance?')
    ab1 = float(input())
    print('What is your available margin?')
    am1 = float(input())
    print('How much leverage do you have? If 50:1, put 50. If 1:1, put 1.')
    l1 = float(input())
    print('Your Trade size should be:')

    if tsl == 'c':
        print((l1 * (ab1 - (ab1 - am1))) / 20)
    if tsl == 'b':
        print((l1 * (ab1 - (ab1 - am1))) / 10)
    if tsl == 'a':
        print((l1 * (ab1 - (ab1 - am1))) / 5)
while True:
    tsl()