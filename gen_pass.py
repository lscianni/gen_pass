#!/usr/bin/env python3

"""
  Password generator
  Generates 8 character passwords With 
  one capital letter one special character
  and one integer
  11/14/2017
  Louis Scianni
"""

import openpyxl
import random
import os
from sys import argv

def make_pass():
    spreadsheet = argv[1]                                                               # get our spreadsheet file from commandline argunemt
    sp_char = ['!', '@', '#', '$', '%', '^', '&', '*']                                  # an array of special characters
    rand_digit = random.randint(0, 9)                                                   # get random number between 0 and 9
    cells = random.randint(0, 200)                                                      # randomly choose a cell from csv file
    
    wb = openpyxl.load_workbook(spreadsheet)   # open the file                          
    sheet = wb.get_sheet_by_name('Sheet1')     # select the sheet we are going to use

    spchar = sp_char[random.randint(0, 7)]     # choose a random integer
        
    word = sheet['A%s' % cells].value          # choose a random word
    cap_word = word.title()#word.replace(word[0], word[0].upper()) # capatilize the letter
 
    
        
    print('%s%s%d' % (cap_word, spchar, rand_digit)) # print the word

make_pass()  # call our function
