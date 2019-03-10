#!/usr/bin/env python
#
# Scrape a word from freedictionary.com and create a password with the
# minimum complexity requirements
#
# 04/24/2018
"""
    Copyright (C) 2019  Louis Scianni

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

        lscianniit@gmail.comm

"""

import requests, random
from lxml import html
from sys import argv

def get_args():
    try:
        num_words = argv[1]
    except IndexError:
        num_words = 1
    return int(num_words)
    
def gen_pass():
    num = get_args()
    url = 'https://www.thefreedictionary.com/8-letter-words.htm'
    
    sess = requests.Session()
    
    response = sess.get(url)
    
    tree = html.fromstring(response.content)
    
    words = tree.xpath('//div[@class="TCont"]/ul/li/a/text()')
    #print(len(words))
    for word in range(0, num):
        word = words[random.randint(0, len(words)-1)]
        sp_char = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', '<', '>', '(', ')', '+', '_', '-', '='] 
        passwd = '%s%s%d' % (word.title(), sp_char[random.randint(0, len(sp_char)-1)], random.randint(0, 10))
        #passwd = '%s%d' % (word.title(), random.randint(0, 10))
        print(passwd)
   
if __name__ == '__main__':
    gen_pass()
