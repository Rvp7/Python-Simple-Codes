#A Program to read and split list-Assignment 8.4
fhand=open('romeo.txt')
z=list()
for line in fhand:
    y=line.split()
    z=z+y
z.sort()
z.append("-sorted by Ravikant")
print(z)

#Method 2 acoording to given
#I was needed to type it again even though I have defined fhand earlier
fhand=open('romeo.txt')
a=list()
for line in fhand:
    for word in line.split():
        if word in a:
            continue
        else:
            a.append(word)
a.sort()
print(a)