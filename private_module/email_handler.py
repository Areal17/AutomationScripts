import smtplib
import ssl
import private_module.credetials as credetials


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
        message = """\
            Subject: Hallo Ingo 

            Ich habe es offensichtlich geschaft. Ein Mail ging raus """
        print(self.sender_mail)
        try:
            server = smtplib.SMTP("smtp.1und1.de", self.port)
            server.ehlo()
            server.starttls(context=self.context)
            server.ehlo()
            server.login(self.sender_mail,self.password)
            server.sendmail(self.sender_mail,receiver_mail,message)
        except Exception as expection:
            print(expection)
        finally:
            server.quit()
        
        # with smtplib.SMTP_SSL("smtp.1und1.com",self.port, context=self.context) as server:
        #     server.login(self.sender_mail,self.password)
        #     server.sendmail(self.sender_mail,receiver_mail,message)
