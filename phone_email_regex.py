# This program extracts Nigerian phone numbers and any
# email addresses from a text.
# Here's what it will do: 
# - copy the text from the clipboard
# - find all NG phone numbers and email addresses
# - neatly format and paste them in the clipboard

import pyperclip 
import re

# Create the NG phone number regex
ngphone_regex = re.compile(r'(0)(7|8|9)(0|1)(\d{8})') 

#Create email regex
email_regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+     # username
            @                     # @ symbol
            [a-zA-Z0-9.-]+        # domain name
            (\.[a-zA-Z]{2,4})     # dot-something
                
    
)''', re.VERBOSE)


# Find matches in the clipboard
text = str(pyperclip.paste())
matches = []
for group in ngphone_regex.findall(text):
    number = ''.join([group[0], group[1], group[2], group[3]])
    matches.append(number)
for group in email_regex.findall(text):
    matches.append(group[0])


# Copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')




