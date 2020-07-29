import smtplib
import ssl
import private_module.credetials as credetials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailHandler:

    port = None
    context = None
    password = ""
    sender_mail = ""

    def __init__(self):
        sender, pw = credetials.credetials_for_mail()
        self.password = pw
        self.sender_mail = sender
        self.port = 587
        self.context = ssl.create_default_context()
    

    def sendMail(self):
        receiver_mail = "wiederoder@areal-17.com"
        #Multipart - für mehrere MIME-Typen
        message = MIMEMultipart("alternative")
        message["Subject"] = "Mail von Python"
        message["From"] = "BFVario_Newsletter@htw-berlin.de"
        message["To"] = receiver_mail
        # Message kann auch HTML enthalten
        text = """\
            Hallo Ingo

            Dies Mail ist per Script verschickt worden. Wenn du dies liest, hat das Script funktioniert.

            VG
            Python-Script
            """
        # MimeText erzeugen 
        mail_text = MIMEText(text)
        message.attach(mail_text)
        print(self.sender_mail)
        try:
            server = smtplib.SMTP("smtp.1und1.de", self.port)
            server.ehlo()
            server.starttls(context=self.context)
            server.ehlo()
            server.login(self.sender_mail,self.password)
            server.sendmail(self.sender_mail,receiver_mail,message.as_string())
        except Exception as expection:
            print(expection)
        finally:
            server.quit()
