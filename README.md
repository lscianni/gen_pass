# gen_pass

Generate a random password from a list of words in an excel file.

Will generate a password that is at least 8 characters long with the first letter capitalized, one special character, and one numeric character. 
For example:

"Turtle!9"

#### Required Modules
* openpyxl

#### Usage

Run gen_pass.py with an excel file as an argument.

For example: gen_pass.py wordlist.xls

# gen_pass1

Scrapes freedictionary.com for a 8 letter word and creates a password.

#### Required Modules
* requests
* lxml

#### Usage

gen_pass1
