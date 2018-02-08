# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:59:40 2018

@author: Shingai Shamu
@name : Mocka - Datatypes
@description: Mocka is a library for generating random vars and Objects for use
in Mock Database Generating.
It is the successor of SoshyMock, which was designed for mocking users but was
ultimately lacking in a lot of features.
"""

import random
import datetime
import rstr

def mint(minval, maxval):
    """returns an integer in the range of maxvalue, minvalue"""
    return random.randint(maxval, minval)

def mfloat(minval, maxval):
    """returns a float in the range of maxvalue, minvalue"""
    return random.uniform(maxval, minval)

def mstring(numchars, case='lower', integers=False, punctuation=False):
    """" Generates a random string """
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha_lower.upper()
    integers_str = '0123456789'
    punct_str = '`~!@#$%^&*()_+=-{}[]:;,.<>?/|"'
    seq = ''
    str_choice = ''
    # check for case type
    if case == 'lower':
        str_choice += alpha_lower
    if case == 'upper':
        str_choice += alpha_upper
    if case == 'mixed':
        str_choice += (alpha_lower + alpha_upper)
    if integers is True:
        str_choice += integers_str
    if punctuation is True:
        str_choice += punct_str
    # add the sequence to a string
    for i in range(numchars):
        seq += random.choice(str_choice)
        print(i)
    #finally return the var
    return seq

def mdate(mindate, maxdate):
    """returns a date in the range DD-MM-YYYY up to DD-MM-YYYY"""
    sys_random = random.SystemRandom()
    random.seed()
    min_val = mindate.split('-')
    max_val = maxdate.split('-')
    day = sys_random.randint(int(min_val[0]), int(max_val[0]))
    month = sys_random.randint(int(min_val[1]), int(max_val[1]))
    year = sys_random.randint(int(min_val[2]), int(max_val[2]))
    return datetime.date(year, month, day)

def marray(num, funct):
    """tranforms stuff into an array"""
    random.seed()
    return [funct for x in range(num)]

def mregex(regex):
    """
    Generates text based on simplified regular expression syntax
        [A-Z][a-z][0-9]
        {4}[A-Z]
        @,:
        whitespace
    """
    uni_reg = rstr.xeger(regex)
    return str(uni_reg)
