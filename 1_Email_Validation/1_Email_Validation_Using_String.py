"""
Basic things in email are:
@ use only once
you should have lower letter but not have upper case letter
use only (_ symbols & . symbols) not any other symbols and (. symbol position should be third/fourth position)
don't use special characters like has & and
can't use space
"""


print("\n")  # Program to find Email Validation (by using special conditions)
email = input("Enter your Email : ")  # g@g.in, wscube@gmail.com
k, j, d = 0, 0, 0
if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if ("@" in email) and (email.count("@") == 1):  # 3
            if (email[-3] == ".") ^ (email[-4] == "."):  # (^/xor operator)  # 4
                for i in email:
                    if i == i.isspace():  # 5
                        k = 1  # k is denoted for finding space
                    elif i.isalpha():
                        if i == i.isupper():  # 5
                            j = 1  # j is denoted for finding upper alphabets
                    elif i.isdigit():
                        continue  # continue means you can use digit
                    elif (i == "_") or (i == ".") or (i == "@"):
                        continue  # continue means you can use all these three signs in your email
                    else:  # 5
                        d = 1  # d is used when you get any other sign except these three then d will become 1

                if (k == 1) or (j == 1) or (d == 1):
                    print("Wrong Email 5 Condition")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4 Condition")
        else:
            print("Wrong Email 3 Condition")
    else:
        print("Wrong Email 2 Condition")
else:
    print("Wrong Email 1 Condition")


# convert python program to app
# live python program
# use python in frontend
# python coding example solve suing DSA, and project ideas
# what skills and knowledge can be uploaded and use for my space and climate filed (also focus on that)
