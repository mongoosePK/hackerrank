# william pulkownik
# day28RegEx.py
# practice filtering gmail addresses from a list using regular expressions

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    # create list to store gmail users
    # then compile a regular expression to match 
    gmailUsers = []
    p = re.compile('@gmail.com', re.IGNORECASE)

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if p.search(emailID):
             gmailUsers.append(firstName)

    [print(name) for name in sorted(gmailUsers)]
    