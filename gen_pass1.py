#!/usr/bin/env python
#
# Scrape a word from freedictionary.com and create a password with the
# minimum complexity requirements
#
# Louis Scianni
# 04/24/2018

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