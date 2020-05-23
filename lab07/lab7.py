#!/usr/bin/env python3

from mymod import Draw
from mymod import ArabicToRoman
from mymod import RomanToArabic

#1:
number=1961
print(f"number={number}")
print(f"ArabicToRoman: {ArabicToRoman(number)}")

#2:
print(f"RomanToArabic: {RomanToArabic(ArabicToRoman(number))}")

#3:
Draw(1) #n=1
Draw(3) #n=3
Draw(5) #n=5
Draw(7)