#Assignment 6.5-Python for everybody
str='X-DSPAM-Confidence: 0.8475 '
a=str.find(' ')
b=str[a:]
c=b.strip()
#No need to write line 5,pyhton neglects space.
d=float(c)
print(d)