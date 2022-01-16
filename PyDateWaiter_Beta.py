# Version : Beta
# Author : wallga
# Build for Python 3.x

import datetime

# Time valuables
now = datetime.datetime.now()       
nowY = now.year
nowM = now.month
nowD = now.day
nowh = now.hour
nowm = now.minute


anniv_name = input("Anniversary Name : ")
anniv = input("Anniversary Date : ") # 8 
annivY = anniv[0:4]
annivM = anniv[4:6]
annivD = anniv[6:]
anniv_tuple = (annivY, annivM, annivD, 0, 0, 0)

# Int Error 
try:
    int(anniv)
    annivInt = True
except ValueError:
    annivInt = False
if annivInt == False:
    print("ValueError : Anniversary date must be number. (ex:080701)")
    exit()

# Calculate Code
nthY = int(nowY) - int(annivY)
diffrenceD = (anniv_tuple - now)
print(diffrenceD)

# Decide Code
while True:
    if nowY != annivY and nowM == annivM and nowD == annivD:
        print("Today is {0}th {1}! Congratulations!".format(nthY, anniv_name))
    elif nowY == annivY and nowM == annivM and nowD == annivD:
        print("Today is {0}!".format(anniv_name))
    else:
        print("There are {0} days left until the anniversary.") 