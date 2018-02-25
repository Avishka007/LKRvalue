import re
import urllib.request
import datetime
import time
import csv
import threading
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style




bb=time.time()

today=datetime.date.today()
q="a"
dat= today.weekday()
if dat==0:
        q="monday"
elif dat==1:
        q="tuesday"
elif dat==2:
        q="wednesday"
elif dat==3:
        q="thursday"
elif dat==4:
        q="friday"
elif dat==5:
        q="saterday"
else:
        q="sunday"
                

print("today is : " , today ," " , q.upper() ,"||| time : " ,  datetime.datetime.now().time())
time_1 = today ,   datetime.datetime.now().time()


#url= https://finance.google.com/finance?q=LKRGBP
y="s"
url="https://finance.google.com/finance?q="

cur=["LKRGBP","LKRUSD","LKREUR","LKRJPY","LKRAUD","LKRCAD","LKRINR"]

for i in cur:
    y=i
    #print(y)
    aaa=time.time()
    url1=url+y
    #print(url1)

    if y=="LKRGBP":
        r="Sri Lanka Rupee to British Pound (£)"
    elif y=="LKRUSD":
        r="Sri Lanka Rupee to US Dollar ($)"
    elif y=="LKREUR":
        r="Sri Lanka Rupee to Euro (€)"
    elif y=="LKRJPY":
        r="Sri Lanka Rupee to Japanese Yen (¥)"
    elif y=="LKRAUD":
        r="Sri Lanka Rupee to Australian Dollar (A$)"
    elif y=="LKRCAD":
        r="Sri Lanka Rupee to Canadian Dollar (CA$)"
    else:
        r="Sri Lanka Rupee to Indian Rupee (₹)"

    print("the value of :" , r , " is ;")
    
    data = urllib.request.urlopen(url1).read()
    data1 = data.decode("utf-8")
    #print (data1)

    m = re.search('meta itemprop="price"',data1)    #price
    n = re.search('meta itemprop="priceChange"',data1)   #price change
    o = re.search('meta itemprop="priceChangePercent"',data1)  #priceChangePercent


    start0 = m.start()
    end0 = start0+50

    start1 = n.start()
    end1 = start1+59

    start2 = o.start()
    end2 = start2+70

    new0=data1[start0:end0]
    new1=data1[start1:end1]
    new2=data1[start2:end2]

    #print(new0,new1,new2)

    #number slicing
    #for 0 th item
    m=re.search('content="',new0)
    start=m.end()
    newnew0=new0[start:]

    m=re.search('" />',newnew0)
    end = m.end()-4
    final0=newnew0[0:end]
    print("One sri lanka rupee is equal to :", final0)

    #for 1 st item
    n=re.search('ontent="',new1)
    start=n.end()
    newnew1=new1[start:]

    n=re.search('/',newnew1)
    end=n.end()-3
    final1=newnew1[:end]
    print("price change is :",final1)

    #for 2 rd item
    o=re.search('content="',new2)
    start=o.end()
    newnew2=new2[start:]

    o=re.search('/',newnew2)
    end=o.end()-3
    final2=newnew2[:end]
    xyz=float(final0)
    print("price change percentage is :",final2)
    print("1000 sri lankan rupees would be :" , xyz*1000, y[3:])
    aaaa=time.time()
    print("time taken to process data :", float(aaaa-aaa))
    print("===============================================================================")

    nigga = float(aaaa-aaa)
#the array for the csv writter
    man = [time_1,xyz,final0,final1,final2,nigga]
#in each loop the csv writer will write a new row to csv
    with open ("finance.csv", "a") as csv_file:
            csv_app = csv.writer (csv_file)
            csv_app.writerow (man)

    



bbb=time.time()
diff=float(bbb-bb)
print("total time to process stock data :",  diff)

if diff>35:
    print ("too long to get accurate data; plz restart the process")
else:
    pass





