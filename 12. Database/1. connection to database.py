# importing the mysql connection library
import mysql.connector
from mysql.connector import errorcode

con = mysql.connector.connect(host='localhost', user='root')
cursor = con.cursor()


DB_NAME = 'employees'
TABLES = {}
TABLES['employees'] = (
 "CREATE TABLE `employees` ("
 " `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
 " `birth_date` date NOT NULL,"
 " `first_name` varchar(14) NOT NULL,"
 " `last_name` varchar(16) NOT NULL,"
 " `gender` enum('M','F') NOT NULL,"
 " `hire_date` date NOT NULL,"
" PRIMARY KEY (`emp_no`)"
 ") ENGINE=InnoDB")
TABLES['departments'] = (
 "CREATE TABLE `departments` ("
 " `dept_no` char(4) NOT NULL,"
 " `dept_name` varchar(40) NOT NULL,"
 " PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
 ") ENGINE=InnoDB")
TABLES['salaries'] = (
 "CREATE TABLE `salaries` ("
 " `emp_no` int(11) NOT NULL,"
 " `salary` int(11) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date NOT NULL,"
 " PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
 " CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
 " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")
TABLES['dept_emp'] = (
 "CREATE TABLE `dept_emp` ("
 " `emp_no` int(11) NOT NULL,"
 " `dept_no` char(4) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date NOT NULL,"
 " PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
 " KEY `dept_no` (`dept_no`),"
 " CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
 " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
 " CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
 " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")
TABLES['dept_manager'] = (
 " CREATE TABLE `dept_manager` ("
 " `emp_no` int(11) NOT NULL,"
 " `dept_no` char(4) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date NOT NULL,"
 " PRIMARY KEY (`emp_no`,`dept_no`),"
 " KEY `emp_no` (`emp_no`),"
 " KEY `dept_no` (`dept_no`),"
 " CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
 " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
 " CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
 " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")
TABLES['titles'] = (
 "CREATE TABLE `titles` ("
 " `emp_no` int(11) NOT NULL,"
 " `title` varchar(50) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date DEFAULT NULL,"
 " PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
 " CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
 " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")


def createDatabase(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf-8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed Database Creation: {}".format(err))
        exit(1)

createDatabase(cursor)

try:
    cursor.execute("USE {}".format(DB_NAME))

except mysql.connector.Error as err:
    print("Database {} does not exist.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database {} created successfully.".format(DB_NAME))
        con.database = DB_NAME
    else:
        print(err)
        exit(1)
        



con.close()


    
    
    