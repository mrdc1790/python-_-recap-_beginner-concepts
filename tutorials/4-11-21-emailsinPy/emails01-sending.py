import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587) #465 or no num
print(smtp_object.ehlo())
smtp_object.starttls()

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
print(smtp_object.login(email,password))

from_address = email
to_address = 'lisapollack@comcast.net'
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = "Subject: "+subject+"\n"+message

smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()