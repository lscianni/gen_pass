#!/usr/bin/env python3

"""
  Password generator
  Generates 8 character passwords With 
  one capital letter one special character
  and one integer
  11/14/2017

    Copyright (C) 2019 Louis Scianni

         This program is free software; you can redistribute it and/or modify
         it under the terms of the GNU General Public License as published by
         the Free Software Foundation; either version 2 of the License, or
         (at your option) any later version.

         This program is distributed in the hope that it will be useful,
         but WITHOUT ANY WARRANTY; without even the implied warranty of
         MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
         GNU General Public License for more details.

         You should have received a copy of the GNU General Public License along
         with this program; if not, write to the Free Software Foundation, Inc.,
         51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

         lscianniit@gmail.com
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
