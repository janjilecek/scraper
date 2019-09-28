# -*- coding: utf-8 -*-
import emailer
import scraper


def main():
    scr = scraper.Scraper()
    sms = emailer.Emailer("fakename", "fakepassword")
    scr.run()
    sms.sendSMS("fakenumber", scr.getPreparedMessage())


if __name__ == '__main__':
    main()


