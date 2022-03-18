import random
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

def mail_send():
    try:
        fromaddr = "your email"
        toaddr = "recipient's email"
        msg = MIMEMultipart()

        msg['From'] = fromaddr 
        msg['To'] = toaddr
        msg['Subject'] = "passwd"

        body = "\nYour passwords of this time."

        msg.attach(MIMEText(body, 'plain'))

        filename = 'passwords.txt'

        attachment = open('passwords.txt','rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.outlook.com', 587) #you can change the email service.
        server.starttls()
        server.login(fromaddr, "Your email password.")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('\nEmail successfully sent.')
    except:
        print("\nError while sending the email.")

init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n4 - send your passwords to your email\n'))
access_ID = 'M4STER001' # You can change this ID.

while True:
    if init == 1:
        obj = input('Define a name to the password: ')
        generator()
        save()
        repeater = input('Do you want to continue? (y/n) ').strip()
        repeater.lower()
        if repeater == 'yes' or repeater == 'y':
            init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n4 - send your passwords to your email\n'))
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
                init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n4 - send your passwords to your email\n'))
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
                init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n4 - send your passwords to your email\n'))
            else:
                print('Ok, thanks.')
                break
        else:
            print("ERROR\nINVALID PASSWORD")
    elif init == 4:
        mail_send()
        repeater = input('Do you want to continue? (y/n) ').strip()
        repeater.lower()
        if repeater == 'yes' or repeater == 'y':
            init = int(input('What do you want to do: \n1 - Generate new password\n2 - See your passwords\n3 - Clear document\n4 - send your passwords to your email\n'))
        else:
            print('Ok, thanks.')
            break


