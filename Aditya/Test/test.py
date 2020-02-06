__author__ = 'Aditya Roy'

# var1 = "Guru99!"
# var2 = "Software Testing"
# print ("var1[0]:",var1[0])
# print ("var2[1:5]:",var2[1:5])
# print ("l" in var1)
# print ("xxx"+var1+"xxx")
#
# print (var2*8)
# tuple  = ('aditya','7501451160','raiganj')
# print (tuple[1])
# (name,phone,place)=tuple
# print (name)


# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print (Dict['Tim'])
# Dict.update({'Aditya':27})
# print (Dict)
# del Dict['Charlie']
# print ("Dic is: %s" % Dict.items())


# import re
# xx = "guru99,education is fun"
# r1 = re.findall(r"^\w+", xx)
# print (re.split(r'\s','we are splitting the words'))
# print (re.split(r's','split tshe words'))
#
# import calendar
# c = calendar.HTMLCalendar(calendar.SUNDAY)
# str = c.formatmonth(2017,1)
# print (str)

# f = open("D:/NIKON D90_Important/DinnerClub.txt","r")
# if f.mode == 'r':
#     contents = f.read()
#     print (contents)


import os
import shutil
from os import path

def main():
    if path.exists("DinnerClub.txt"):
        src = path.realpath("D:/NIKON D90_Important/DinnerClub.txt");
        head,tail = path.split(src)
        print (head)
        print (tail)
        print (src)
if __name__== "__main__":
    main()










