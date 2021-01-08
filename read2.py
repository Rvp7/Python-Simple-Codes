#Assignement 7.2- Program to look for lines
file=input("Enter the file name:")
fhandle=open(file)
count=0
sum=0.0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        x=line[20:]
        y=float(x)
        sum=sum+y
        count=count+1
print(sum,count)
print("Average spam confidence:",sum/count)