#LINK: https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
if n%2==1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6<= n <= 20:
    print("Weird")
else:
    print("Not Weird")

 
#LINK: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
          
    
    return leap

