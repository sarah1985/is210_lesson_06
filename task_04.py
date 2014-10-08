#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 04: Cracking Passwords """

import data
SALT = 'monosodium-glutamate'


def test_passwords(password_list):
    """tests passwords for strength"""

    new_list = []
    for line in password_list:
        temp_list = line.split(":")
        cracked = crack_it(temp_list[1])
        if cracked is not None:
            new_list.append((cracked, temp_list[4]))
    return new_list


def crack_it(hashed_password):
    """compares input to hashed passwords"""

    for word in data.WORDS:
        if data.crypt(word, SALT) == hashed_password:
            return word


def report(weak_passwords):
    """displays report of weak passwords"""

    weak_passwords = test_passwords(data.PASSWD)
    password = [x[0] for x in weak_passwords]
    name = [x[1] for x in weak_passwords]
    if weak_passwords is not None:
        return """
        Cracked passwords
        --------------------------------------
        """

REPORT = report(test_passwords(data.PASSWD))
print REPORT


#if __name__ == "__main__":
 #   print crack_it('ckRzvUxfMC2KC4ENIyRRSiC1eZQ=')
  #  print test_passwords(data.PASSWD)