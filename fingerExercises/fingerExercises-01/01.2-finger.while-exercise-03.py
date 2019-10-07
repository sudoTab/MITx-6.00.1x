#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:41:47 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
01.2-Finger While Exercise 03
----------------------------
3. Write a while loop that sums the values 1 through end, inclusive. 

end is a variable that we define for you. 

So, for example, if we define end to be 6, your code should print out the result:

    21

which is 

    1 + 2 + 3 + 4 + 5 + 6.

Note:
For problems such as these, do not include input statements or define variables we will provide for you.
"""

"""Answer Script:"""
total = 0
i = 0

while i <= end:
    total += i
    i += 1

print(total)
