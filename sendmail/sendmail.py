from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mailserver = 'mail.pearsolution.com.ua'
port = '25'

msg = MIMEMultipart()
msg['From'] = 'office@pearsolution.com.ua'
msg['To'] = 'office@pearsolution.com.ua'
msg['Subject'] = "WARNING!!!"
#password = "Lelikbolik2091"
password = "Y3j2C1b1"

body = "\n Здравствуйте, Pear Solution! " \
       "\n Поздравляем, вы доигрались с вашими дос-атаками, Ваша почта взломана! " \
       "\n Вам трындец " \
       "\n <a href=""https://pearsolution.com.ua"">You can bild the best site in the world with us!!</a>"
msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP(mailserver, port)
#server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

