import smtplib

mailserver ='mail.pearsolution.com.ua'
port = '25'
mailfrom = 'almonah@pearsolution.com.ua'
password = 'Lelikbolik2091'
mailto = 'iskripnichenko@pearsolution.com.ua'
content = 'Hello world'


server = smtplib.SMTP(mailserver, port)
#server.connect('mail.pearsolution.com.ua', 25)
#server.starttls()
server.login(mailfrom, password)
server.sendmail(mailfrom, mailto, content)
server.quit()
