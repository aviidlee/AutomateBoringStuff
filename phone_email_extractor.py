#! python3
#
# Code partly taken from: https://automatetheboringstuff.com/chapter7/
#
# Find all phone numbers and emails addresses in clipboard contents, then paste
# extracted content back into clipboard.

import pyperclip, re, string

phoneReg = re.compile(r'''(
    (\+\d{1,3})? # Optional country code
    (\s|-|\.)?   # Separator
    (\d{1,2})?   # Optional area code
    (\s|-|\.)? 
    (\d{3,4})    # Australian landline format
    (\s|-|\.)
    (\d{3,4})
    )''', re.VERBOSE)

# Fairly loose regex because don't know all the strict rules for email address format
emailReg = re.compile(r'''(
    \w+          # Assume emails must begin with alphanum
    [\w._-]*    # Then after that it is allowed to have certain punctuation
    @\w+.\w+    # Domain name - not very restrictive but meh.
    )''', re.VERBOSE | re.I) 

# Get matches from clipboard text
text = str(pyperclip.paste())
matches = []

# Put all numbers in the format 
# [<+countrycode>] [(<area code>)] <numbers> <numbers> <numbers>

for groups in phoneReg.findall(text):
    print groups
    phoneNum = string.join((groups[5], groups[7]), ' ')
    
    countryCode = ''
    areaCode = ''

    # Country code present
    if groups[1] != '':
        countryCode = groups[1]

    # Area code present
    if groups[3] != '':
        areaCode = '({})'.format(groups[3])

    phoneNum = '{} {} {}'.format(countryCode, areaCode, phoneNum)
    matches.append(phoneNum)

for groups in emailReg.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')