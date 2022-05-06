import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendemail(address):
    reg = "^[a-zA-z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,address)):
        smtp.send_message(msg)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")
    
msg = EmailMessage()
msg.set_content("부기온앤온")

msg["Subject"] = "제목"
msg["From"] = "rivsh030@likelion.org"
msg["To"] = "alphago@gmail.com"

with open("boogie.png","rb") as img:
    img_file = img.read()
img_type = imghdr.what("boogie",img_file)

msg.add_alternative(img_file,maintype="image",subtype=img_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("rivsh030@likelion.org","##########")
sendemail("rivsh030@likelion.org")
smtp.quit()