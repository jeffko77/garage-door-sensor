from gpiozero import Button
from time import sleep
#use GPIOzero to address GPIO ports

#bring in environment variables
import os

def sendEmail():
    import smtplib

    gmail_user = os.environ['GUNAME']
    gmail_password = os.environ['GPW'] 

    from1 = '8SommeCourt'
    #to = '3142651807@tmomail.net'  
    to = 'jeffko77@gmail.com'
    subject = 'Garage Door is open'  
    body = 'Garage Door is open'

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (from1, to, subject, body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from1, to, email_text)
        server.close()

        print 'Email sent!' 
    except:  
        print 'Something went wrong...'


mag_sensor = Button(6) #GPIO 6 should be used for the magnet.

#by default, it is open when the magnet is aligned. sense the magnet is missing.

if mag_sensor.value == False:
    #sleep 600
    sendEmail()


