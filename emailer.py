# -*- coding: utf-8 -*-
import smtplib


class Emailer:
    def __init__(self, email, password):
        self.email = email
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(email, password)

    def sendSMS(self, number, text):
        print(text)
        self.server.sendmail(self.email + "@gmail.com", number + "@SMS.t-mobile.cz", "\n" + text)
