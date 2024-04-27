import smtplib, os
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import passss
from captcha.image import ImageCaptcha
from random import choice


def send_email(to_addr, subject, text):
    pattern = []
    for i in range(8):
        pattern.append(choice(simple).lower())
        ss = ''.join(pattern)
        with open('pat.txt', 'w') as file: file.write(ss)
    image_captcha = ImageCaptcha(width=300, height=200)
    image_captcha.write(pattern, 'captcha.png')

    filepath = 'captcha.png'
    basename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
    part_file.set_payload(open(filepath, "rb").read())
    part_file.add_header('Content-Description', basename)
    part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
    encoders.encode_base64(part_file)


    msg = MIMEMultipart()
    msg['From'] = passss.login
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(
        MIMEText(text, 'plain')
    )
    msg.attach(part_file)

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(passss.login, passss.password)
    server.ehlo(to_addr)
    server.auth_plain()
    server.send_message(msg)
    server.quit()


def pat():
    with open('pat.txt', 'r') as file:
        pat = "".join(file.read())
    return pat


simple = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
          'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
          '4', '5', '6', '7', '8', '9', '0']
