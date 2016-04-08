import itertools
import sys
import re



pattern = [
             "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ,
             "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ,
             "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ,
             "M", "MM", "MMM","LXVI"
        ]

roman = input("type roman Num:   ")
if pattern.index(roman):
    print (roman + " it's true")
else:
    print ("False")
