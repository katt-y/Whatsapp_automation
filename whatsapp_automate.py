import re
from alright import WhatsApp

from selenium import webdriver

import time

## open the CSV and extract numbers from the file

d=open('Customers_Report.csv','r')
m=d.readlines()

list_1=[]
for i in m:
    list_1.append([i])

int_list = []
for i in range(10):
    int_list.append(str(i))


number_list=[]

for i in m:
    for k in range(len(i)-9) :
        if i[k] not in int_list:
            continue;
        elif i[k] in int_list:
            if i[k+9] in int_list:
                number_list.append(i[k:k+10])
            else:
                continue   

                



number_list_2=[]
for i in number_list:
    if ' ' not in i:
        number_list_2.append(i)
        



 





## Removing invalid numbers



def isValid(s):
	
	
	Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
	return Pattern.match(s)


s = "9911918042"
if (isValid(s)):
	print ("Valid Number")	
else :
	print ("Invalid Number")




s =  number_list_2
valid=[]
for i in s:
    
     
    if (isValid(i)):
        
        valid.append(i)
    else:
        continue



##  Sending the messages to each of these customers.


browser = webdriver.Chrome()
messenger=WhatsApp(browser=browser)




for i in valid :
 messenger.find_user(i)
 time.sleep(6)
 messenger.send_video('/Users/kumarkatyayanjaiswal/Desktop/cafe_work/lohri.JPG')

 time.sleep(6)
 

    


    
