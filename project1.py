import os

'''
# Clearing the Screen
os.system('clear')
'''

def calculate(num1, num2, symbol):
    num1

print(
    r'''db   db d88888b db      db       .d88b.       db   d8b   db  .d88b.  d8888b. db      d8888b. 
88   88 88'     88      88      .8P  Y8.      88   I8I   88 .8P  Y8. 88  `8D 88      88  `8D 
88ooo88 88ooooo 88      88      88    88      88   I8I   88 88    88 88oobY' 88      88   88 
88~~~88 88~~~~~ 88      88      88    88      Y8   I8I   88 88    88 88`8b   88      88   88 
88   88 88.     88booo. 88booo. `8b  d8'      `8b d8'8b d8' `8b  d8' 88 `88. 88booo. 88  .8D 
YP   YP Y88888P Y88888P Y88888P  `Y88P'        `8b8' `8d8'   `Y88P'  88   YD Y88888P Y8888D' 
                                                                                             
                                                                                             '''
)
print('This program is only to specific age group.\n')
age = int(input('Verify your age :'))
while True:
    print('Are you ' + str(age) + ' years old? (Y/N)')
    ageconform = input().lower()

    if ageconform == 'y' or ageconform == 'yes':
        
        if age < 18:
            print('Too soon for you!')
        elif age >= 18 and age < 65:
            print('Wait untill you are older!')
        else:
            print('Alright...')
            print(r'''
Here is what I can do for you:

+ for addition
- for subtraction
* for multiplation
/ for division
            ''')
            choice = input('what do you want to do?')
            if choice == '+':
                num1 = int(input('Please type the first number.'))
                num2 = int(input('Please type the second number.'))
                print('The answer is ')
            elif choice == '-':
                num1 = int(input('Please type the first number.'))
                num2 = int(input('Please type the second number.'))
            elif choice == '*':
                num1 = int(input('Please type the first number.'))
                num2 = int(input('Please type the second number.'))
            elif choice == '/':
                num1 = int(input('Please type the first number.'))
                num2 = int(input('Please type the second number.'))
            else:
                print(r'''I don't understand what do you mean, please type again.''')
            break
    elif ageconform == 'n' or ageconform == 'no':
        age = int(input('Verify your age again:'))
    else:
        print('You can only type yes or no!')
        print('Are you ' + str(age) + ' years old? (Y/N)')
        ageconform = input().lower
