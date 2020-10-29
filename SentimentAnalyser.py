#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:42:18 2020

@author: apple
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']



def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char, '')

    return str1


def get_neg(str1):
    str1 = strip_punctuation(str1)
    str1_lst = str1.split()
    count = 0
    for word in str1_lst:
        if  word in negative_words:
            count = count + 1

    return count

  
def get_pos(str1):
    str1 = strip_punctuation(str1)
    str1_lst = str1.split()
    count = 0
    for word in str1_lst:
        word = word.lower()
        if word in positive_words:
            count = count + 1
    return count


def net_score(str1):
    return get_pos(str1) - get_neg(str1)

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
            
 

with open('project_twitter_data.csv', 'r') as inp:
    with open('resulting_data.csv', 'w') as outp:
        # Header
        Header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score"
        outp.write(Header)
        outp.write("\n")
        
        lins = inp.readlines()
        lins.pop(0)
        # Columns
        for lin in lins:
            cols = lin.strip().split(',')
            outp.write("{}, {}, {}, {}, {}".format(cols[1],(cols[2]), get_pos(cols[0]), get_neg(cols[0]), net_score(cols[0])))
            outp.write("\n")
            
            
    
    
    

