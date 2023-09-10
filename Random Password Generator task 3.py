import random
from datetime import datetime

def random_pwd():
    print('\n\n####################')
    print('Random Password Generator:\n ')
    print('Press 1 for generate new password')
    print('Press 2 for show all password')
    choice =int(input('\nEnter your choice:'))
    if choice == 1:
        alphabats= 'abcdefghijklmnopqrstuvwxyz'
        alphabats+=alphabats.upper()
        number=str('1234567890')
        special_number='@#$_&%?!'
        length= int(input('Enter length of the password: '))
        combination=alphabats+number+special_number
        pwd="".join(random.sample(combination,length))
        print('\nYour generated password is '+pwd)
        with open('password.txt','a') as f:
            f.write('\n'+pwd +'   : length :  ' +str(length) +'  : date : '+ str(datetime.now()))
        random_pwd()
    elif choice ==2:
            print('\nShow all password: \n')
            with open('password.txt','r') as fp:
                print(fp.read())
            random_pwd()
    else:
        exit()

random_pwd()
