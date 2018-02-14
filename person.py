# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:59:41 2018

@author: Shingai Shamu
@code: Mocka - Person
"""
from datatypes import *
import random
import pickle
import datetime
from robohash import Robohash
import base64
from io import BytesIO

def create_avatar(unique_hash):
    hashy = "whatever-hash-you-want"
    rh = Robohash(hashy)
    rh.assemble(roboset='set4')
    buff = BytesIO()
    rh.img.save(buff, format="png")
    img_str = base64.b64encode(buff.getvalue())
    return img_str
        

with open('baby_names.pkl', 'rb') as names_dict:
    names_data = pickle.load(names_dict)
    
names_list = list(names_data.keys())

email_provs = ["yahoo","gmail","live","outlook","hotmail","protonmail",
                   "aol","aim","yandex","protonmail", "zohomail", "mail" ]
                   
nats = ['Zimbabwean','South African','Mozambiquean', 'Malawian', 'Bostwanean']

class Person(object):
    def __init__(self, **kwargs):
        self.firstname = random.choice(names_list)
        self.middlename = random.choice(names_list)
        self.surname = random.choice(names_list)
        self.birthdate = mdate('31-12-1978', '31-12-2002')
        self.gender = names_data[self.firstname]
        if self.gender == 'female':
            if self.birthdate < datetime.date(2000,12,31):
                self.maidenname = random.choice(names_list)
        self.idnumber = mregex('[0-9]{2}-[0-9]{7}-[A-Z][0-9]{2}')
        email_extension = random.choice(email_provs) + ".com"
        email_id = random.choice("0000123456789") + random.choice("0123456789")
        self.email = self.firstname + email_id + "@" + email_extension
        self.username = self.firstname[0] + self.middlename[0] + self.surname
        self.cellnumber = mregex('\+2637[0-9]{8}')
        self.twitter = 'https://twitter.com/'+self.firstname + email_id
        self.facebook = 'https://www.facebook.com/'+self.firstname+"_"+self.surname
        self.nationality = random.choice(nats)
        self.city = ''
        self.address = ''
        self.avatar = create_avatar(self.idnumber)
        
        self.__dict__.update(**kwargs)
    
    def __repr__(self):
        pass
        

human = Person()

        