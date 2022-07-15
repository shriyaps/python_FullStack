import pymysql, datetime
import re
import bcrypt
from Register import register
from Login import login


con = pymysql.connect(host = 'localhost', user = 'root', password = '',
                      database = 'usermanagementdb')
# print(con)
print("Database connected!")
cur = con.cursor()


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
