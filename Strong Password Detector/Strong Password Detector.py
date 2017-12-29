# Strong password detector

import re

while True:

    password = input("Enter password")

    if len(password) >= 8:

        if re.search(r'[a-z]', password):

            if re.search(r'[A-Z]', password):

                if re.search(r'[0-9]', password):

                    if re.search(r'\W', password):
                        print ("Your password is strong enough to pass the test!")
                        break
                    else:
                        print ("Just include a special character and you're done!")

                else:
                    print ("Include a digit in your password!")

            else:
                print ("Include an uppercase letter in your password!")

        else:
            print ("Include a lower case letter in your password!")

    else:
        print ("Your password is too short!")