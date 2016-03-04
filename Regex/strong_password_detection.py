# Strong password detection

import re, sys

def main():
    while True:
        password = raw_input('Please enter your proposed password:\n')

        message = is_strong_password(password)
        if message == None:
            print "That is a strong password. Well done."
        else:
            print "Your password has some problems:"
            print message

        print('\n')

def is_strong_password(password):
    
    if(len(password) < 8):
        return "Password too short; must be at least 8 characters."

    regexList = [(r'[A-Z]', 'Password must contain at least one capital letter.'),
        (r'[a-z]', 'Password must contain at least one lowercase letter.'),
        (r'\d', 'Password must contain at least one digit.')
    ]
    
    for test, message in regexList:
        spd = re.compile(test)
        mo = spd.search(password)
        if mo == None:
            return message

    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Entering interactive password strength assessment."
        print "Press ctrl+c to quit."
        main()
    else:
        message = is_strong_password(sys.argv[1])
        if message == None:
            print "Good password."
        else:
            print message