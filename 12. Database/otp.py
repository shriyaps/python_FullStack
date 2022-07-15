import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

code = ''
for i in range(6):
    code += str(random.randint(1,9))
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
        attempts = (3 - tries)
        print("Incorrect code. {} attempt left".format(attempts))
        count += 1

if tries >= 3:
    print("Attempt over")
mailserver.quit()




