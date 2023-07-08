"""
a to z alphabets + small case
0 to 9 digit
. _ (at a time should be 1 before @)
@ should be 1
. position should be second or third position
"""

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# we use this sign "^" for "start with"
# "\" is used for searching any character in regex
# "?" is used for "0 and 1" if condition is True means ". and _" is presented only once so, you will get true but if ". and _" is presented more than 1 so "?" will give an error
# "\w" is used for searching any string
# "\w" is used for searching any "." at the position of {2, 3} + $ sign is used b/c you are searching "." from back side
user_email = input('Enter your email: ')

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
