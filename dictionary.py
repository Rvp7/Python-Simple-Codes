#A program to find out the person with highest emails-9.4
name=input('Enter the file name:')
fhand=open(name)
dictionary=dict()
bigword=None
bigcount=None
for line in fhand:
    if line.startswith('From '):
        z=line.split()
        email=z[1]
        #Idiom:retrive/create/update counter
        dictionary[email]=dictionary.get(email,0)+1
# We can also creat a list first, then list.append(z[1])
for email,count in dictionary.items():
    if bigword is None or count>bigcount:
        bigword=email
        bigcount=count
#print(dictionary)
print(bigword,bigcount)
            
        
        
