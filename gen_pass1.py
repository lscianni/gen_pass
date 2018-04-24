#!/usr/bin/env python
#
# Generate a random word from thefreedictionary.com
# Scrape the word and create a password with the
# minimum complexity requirements
# Louis Scianni
# 04/24/2018

import requests, random, openpyxl, os
from lxml import html


def request_word():
    url = 'https://www.thefreedictionary.com/8-letter-words.htm'
    
    sess = requests.Session()
    
    response = sess.get(url)
    
    tree = html.fromstring(response.content)
    
    words = tree.xpath('//div[@class="TCont"]/ul/li/a/text()')
    
    word_lst= []
    for word in words:
        word_lst.append(word)
        
    scraped_word = words[random.randint(0, len(word_lst))].title() # capitalize word   
    return scraped_word
        


def gen_passwd(word):
    sp_char = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', '<', '>', '(', ')', '+', '_', '-', '='] 
    passwd = '%s%s%d' % (word,sp_char[random.randint(0, len(sp_char))], random.randint(0, 10))
    print(passwd)
    
if __name__ == '__main__':
    gen_passwd(request_word())
