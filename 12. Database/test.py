import pymysql, datetime
import re
import bcrypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

con = pymysql.connect(host = 'localhost', user = 'root', password = '',
                      database = 'usermanagementdb')

print("Database connected!")
cur = con.cursor()


def register():
    
    fname = input("Enter First Name: ")
    lname = input("Enter Last name: ")
    username = input("Enter username: ")
    email = input("Enter email id: ")
    mobile = input("Enter mobile number: ")
    reg_date = input("Enter registration date: ")
    password = input("Enter password: ")
    confirm_pass = input("Re-enter password: ")

    pwd = password.encode()
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())

    select_query = "select * from user where email = %s"
    cur.execute(select_query, (email,))

    try:
        fname, lname, username, emailD, mobileD, hashed, reg_date = cur.fetchone()
        if emailD and mobileD is not None:
            print("User already exists")
    except Exception as e:
        if fname.isalpha() and lname.isalpha():
            fname = fname.title()
            lname = lname.title()
        else:
            print("Invalid name")

        if mobile.isdigit() and len(mobile) == 10:
            print("Valid mobile number")
        else:
            print("Invalid number")

        upper, lower, special_char, number = 0, 0, 0, 0
        if len(password) >= 8:
            for i in password:
                if (i.isupper()):
                    upper += 1
                if (i.islower()):
                    lower += 1
                if (i.isdigit()):
                    number += 1
                if (i == '@' or i == '#' or i =='$' or i == '*' or i == '_'):
                    special_char += 1
        else:
            print("Password should be more than 8 characters")
        if (lower >= 1 and upper >= 1 and number >= 1 and special_char >= 1):
            print("Valid Password")
        else:
            print("Invalid Password")
            
        if '@gmail.com' in email:
            print('Valid Email')
        else:
            print('Invalid Email')

        if password == confirm_pass: 
            insert_query = """insert into user
(fname, lname, username, email, mobile, password, reg_date)
values(%s,%s,%s,%s,%s,%s,%s)"""       
            user_info = (fname, lname, username, email, mobile, hashed, reg_date)
            
            code = ''
            for i in range(6):
                code += str(int(random.random()*10))
                otp = "Your OTP is: " + code
                msg = otp

            # Sending email to registered user.
            msg = MIMEMultipart()
            msg['From'] = 'shriyaps23@gmail.com'
            msg['To'] = 'shriyashetty227@gmail.com'
            msg['Subject'] = 'simple email in python'
            message = otp
            msg.attach(MIMEText(message))

            mailserver = smtplib.SMTP('smtp.mailtrap.io',587)
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
                            
            mailserver.login('4c6cbb7f558c4c', 'f88865df3e2137')

            mailserver.sendmail('shriyaps23@gmail.com','shriyashetty227@gmail.com',msg.as_string())

            count = 0
            tries = 0
            while count < 3:
                a = input("Enter your OTP: ")
                if a == code:
                    print("Code is Verified")
                    
                    break
                else:
                    tries += 1
                    attempts = (3-tries)
                    print("Incorrect code. {} attempt left".format(attempts))
                    count += 1
                    
            if tries >= 3:
                print("Attempt over. No more tries left.")

                
            mailserver.quit()

            cur.execute(insert_query, user_info)
            con.commit()
            print("Successfully Registered!")

        else:
            print("The password does not match")

def login():
    email = input("Enter your email id: ")
    password = input("Enter your password: ")

    pwd = password.encode()
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())

    pwd1 = bcrypt.checkpw(pwd, hashed)

    select_query = "select * from user where email = %s"
    cur.execute(select_query, (email,))

    try:
        fname, lname, username, emailD, mobileD, pwd1, reg_date = cur.fetchone()
        if emailD is not None:
            if pwd1 is True:
                print("User Logged in")
            else:
                print("Wrong Password")
    except Exception as e:
        print("This user does not exist. Register First!")
        register()
       
    
while True:
    print("""Enter choice:
1. User Registration
2. User Login 
3. Forgot Password
4. Quit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        pass
    elif ch == 4:
        break
    else:
        print("Wrong Input")
con.close()



        

        
    



    
