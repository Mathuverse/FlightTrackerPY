import smtplib

MYEMAIL = "Mathudeals@gmail.com"
PASS = "ngzjeqhpuqfwbqja"

class NotificationManager:

    #Fonction from which we will send the user the emails for the flight prices
    def sendEmail(self,msg):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MYEMAIL, PASS)
            connection.sendmail(
                from_addr=MYEMAIL,
                to_addrs="Mathusan54@gmail.com",
                msg=msg
            )
