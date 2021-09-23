from email.mime.text import MIMEText
from smtplib import SMTP
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os


servidor_correo = 'smtp.gmail.com'
puerto = 465
correo_remitente = 'kardexregbogota@gmail.com'
clave ='900276962KOBA'



from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()
print (str(today))
print (str(now))

dias=(today.day)
meses=(today.month)
yer=format(today.year)



print(" val " + str(dias))

if int(dias) <10:
    dias="0"+format(today.day)
else:
    dias=str(format(today.day))
if int(meses)<10:
    meses="0"+str(today.month)
else:
    meses=str(today.month)

     
     
print(str(dias))
print(str(meses))



fromaddr = correo_remitente
toaddr = "jose.lara@koba-group.com"

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Subject of the Mail"

body = "Body_of_the_mail"

msg.attach(MIMEText(body, 'plain'))

filename = "Kardex_monitor22092021.sql"
attachment = open(r"C:\Users\jose.lara\Documents\GitHub\KARDEX_PYTHON\KARDEX\backup_desatendidos\Kardex_monitor22092021.sql", "rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, clave)

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()