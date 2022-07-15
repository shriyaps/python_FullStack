def register():
    
    fname = input("Enter First Name: ")
    lname = input("Enter Last name: ")
    username = input("Enter username: ")
    email = input("Enter email id: ")
    mobile = input("Enter mobile number: ")
    password = input("Enter password: ")
    confirm_pass = input("Re-enter password: ")
    reg_date = input("Enter registration date: ")

##    pwd = bytes(password, 'utf-8')
    pwd = password.encode()
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())

    def name_check(fname, lname):
        if fname.isalpha() and lname.isalpha():
            fname = fname.title()
            lname = lname.title()
        else:
            print("Invalid name")

    name_check(fname, lname)

    def mobile_check():
        if mobile.isdigit() and len(mobile) == 10:
            print("Mobile: ", mobile)
        else:
            print("Invalid number")

    mobile_check()

            
    def pass_check():
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

    pass_check()

    def email_check():
        if '@gmail.com' in email:
            print('Valid Email')
        else:
            print('Invalid Email')

    email_check()
        
    select_query = "select * from user where email = %s"
    cur.execute(select_query, (email,))
    
    try:
        fname, lname, username, emailD, mobileD, hashed, reg_date = cur.fetchone()
        if emailD and mobileD is not None:
            print("User already exists")
    except Exception as e:
        if password == confirm_pass: 
            insert_query = """insert into user
(fname, lname, username, email, mobile, password, reg_date)
values(%s,%s,%s,%s,%s,%s,%s)"""       
            user_info = (fname, lname, username, email, mobile, hashed, reg_date)
            cur.execute(insert_query, user_info)
            con.commit()
            print("Successfully Registered!")
        else:
            print("The password does not match")


