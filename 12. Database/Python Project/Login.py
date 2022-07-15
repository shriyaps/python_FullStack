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
