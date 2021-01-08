#A program to parse the email address-Assignment 8.5
fhand=open('mbox-short.txt')
count=0
for line in fhand:
    if line.startswith('From '):
        z=line.split()
        print(z[1])
        count=count+1
print("Total",count,"email IDs found")