#import csv
#file=open('sample.csv','r')
#with open('sample.csv','w',newline='') as file:
#       data=[
#        [1,'sravani',23],
#        [2,'sravs',24],
#        [3,'srav',20],
     #   ]
    #record=csv.writer(file)
    #record.writerow(['id','name','age'])
    #record.writerows(data)
#import csv
#with open('sample.csv','a',newline='') as file:
#    record=csv.writer(file)
#    record.writerow([4,'vani',21])
#import csv
#with open('sample.csv','r',newline='') as file:
#   record=csv.reader(file)
#    for i in record:
#        print(i)
#import csv
#with open('new.csv','w',newline='') as csvfile:
#    fieldnames=['id','name','age']
#    record=csv.DictWriter(csvfile,fieldnames)
#    record.writeheader()
#    data=[
#        {'id':'1','name':'riya','age':18},
#        {'id':'2','name':'priya','age':19},
#        {'id':'3','name':'sriya','age':20},
#        {'id':'4','name':'diya','age':21},
#    ]
#    record.writerows(data)
import csv
with open('new.csv','r',newline='') as file:
   records=csv.DictReader(file)
   for i in records:
       print(i)

