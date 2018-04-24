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
    spreadsheet = argv[1]                     # get our spreadsheet file from command line argument
    sp_char = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', '<', '>', '(', ')', '+', '_', '-', '='] # an array of special characters
    rand_digit = random.randint(0, 10)                                                   # get random number between 0 and 9
    cells = random.randint(0, 201)                                                      # randomly choose a cell from csv file
    
    wb = openpyxl.load_workbook(spreadsheet)   # open the file                          
    sheet = wb.get_sheet_by_name('Sheet1')     # select the sheet we are going to use

    #spchar = sp_char[random.randint(0, len(sp_char))]     # choose a random integer
        
    word = sheet['A%s' % cells].value          # choose a random word
    cap_word = word.title()#word.replace(word[0], word[0].upper()) # capitalize the letter
 
    
        
    print('%s%s%d' % (cap_word, spchar[random.randint(0, len(sp_char))], rand_digit)) # print the word

if __name__ == '__main__':
    make_pass()  # call our function
