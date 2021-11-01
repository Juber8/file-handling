'''
import csv
with open('student.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['name','roll_no','marks ','adress'])
    while True:
        name=input('enter student name:')
        roll_no=int(input('enter roll no'))
        marks=int(input('enter marks'))
        adress=input('enter your adress:')
        w.writerow([name,roll_no,marks,adress])
        option=input('do  you want add row again:  yes/no:')
        if option.lower()=='no':
            break
print('total student data will be written successfuly')

import csv
f=open('student.csv','r')
r=csv.reader(f)
for i in r:
    print(i)

with open('juber.txt','r+') as f:
    f.write('juber\n')
    f.write('how\n')
    f.write('are\n')
    f.write('you\n')
    print('data written succesfully')

with open('mulla.txt','w') as f:
    list=['juber\n','nilesh\n','akash\n','shubham\n','arbbaj\n']
    f.writelines(list)

f=open('mulla.txt','r')
data =f.readlines()
for i in data:
    print(i,end=' ')

f=open('mulla.txt','r')
data=f.read()
for i in data:
    print(i,end=' ')
'''
