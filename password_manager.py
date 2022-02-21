import random
from time import sleep

def generator():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    sym = '[]{}()*#;/,-_%'

    qnt = int(8)
    length = qnt

    MAXnum = lower + upper + digits + sym
    global passwdMAXnum
    passwdMAXnum = "".join(random.sample(MAXnum, length))
    print(f'Password: {passwdMAXnum}')

def save():
    global passwd_file
    passwd_file = open('passwords.txt', 'a')
    passwd_file.write(obj + ': ')
    passwd_file.write(passwdMAXnum +'\n')
    passwd_file.close()
    sleep(2)
    print('Your password was successfully saved.')

init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n'))
access_ID = 'M4STER001'

while True:
    if init == 1:
        obj = input('Define a name to the password: ')
        generator()
        save()
        repeater = input('Do you want to continue? (y/n) ').strip()
        repeater.lower()
        if repeater == 'yes' or repeater == 'y':
            init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n'))
        else:
            print('Ok, thanks.')
            break
    elif init == 2:
        access_confirm = input("Input the access ID, please:\n")
        if access_confirm == access_ID:
            passwd_file = open("passwords.txt","r")
            string_passwords = passwd_file.read()
            print(string_passwords)
            passwd_file.close()
            repeater = input('Do you want to continue? (y/n) ').strip()
            repeater.lower()
            if repeater == 'yes' or repeater == 'y':
                init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n'))
            else:
                print('Ok, thanks.')
                break
        else:
            print("ERROR\nINVALID PASSWORD")
    elif init == 3:
        access_confirm = input("Input the access ID, please:\n")
        if access_confirm == access_ID:
            passwd_file = open('passwords.txt', 'w')
            passwd_file.close()
            print('Your document has been cleaned.')
            repeater = input('Do you want to continue? (y/n) ').strip()
            repeater.lower()
            if repeater == 'yes' or repeater == 'y':
                init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n'))
            else:
                print('Ok, thanks.')
                break
        else:
            print("ERROR\nINVALID PASSWORD")


