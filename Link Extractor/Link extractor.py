# Link Extractor (for http:// and https:// links only)

"""
Step 1- Copy the text from which you want to extract links to the clipboard
        (ctrl+A to select all)
Step 2- Run program
Step 3- Extracted links are copied to your clipboard, one per line

NOTE: Requires the pyperclip module downloaded in the same folder as the program
"""

import re
import pyperclip

# Creates regex object
linkreg = re.compile(r'''
(
(https:// | http://) # http:// or https://
([a-z]+.)?           # www., en. etc
[a-zA-Z0-9-]+        # host name
\.                   # . symbol
[a-z]{2,4}           # Extension
(/[^/\s]*)*          # Additional
)
''', re.VERBOSE)

# Pastes text from clipboard
text = pyperclip.paste()

# Finds all occurences in copied text
link = linkreg.findall(text)

# Returns a string object in different lines
returnlist = []
for i in link:
    returnlist.append(i[0])
returnstring = '\n'.join(returnlist)

# Pastes to clipboard
pyperclip.copy(returnstring)
