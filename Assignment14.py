'''Q1'''
'''Defining function to read line from last'''
def read_last_lines(filename, lines):
    with open(filename, "r") as text_file:
        '''opening file in read mode'''
        contents = text_file.readlines()[-lines:]
        '''read lines from last'''
        for line in contents:
            print(line, end="")
            '''printig lines'''

'''Main program'''
n = int(input("Enter the Number of lines to be read: "))
'''Taking number of lines from user'''
read_last_lines("assingment.txt", n)
'''Calling funtion to print those lines'''

'''Q2'''
from collections import Counter
'''Import Counter class from collections module to count'''

'''defining function to count words frequency'''
def word_count(fname):
        with open(fname) as f:
            '''opening file in read mode'''
            return Counter(f.read().split())
            '''counting frequencr and storing in a dictionary'''

print("Number of words in the file :",word_count("assingment.txt"))
'''Calling function'''

'''Q3'''
with open('assingment.txt','r') as ff:
    x=ff.read()
'''Opening file in read mode'''
with open('new.txt','w') as zz:
    a=zz.write(x)
'''Opening new.txt in write mode and copying text there'''

'''Q4'''
with open('assingment.txt') as fh1, open('new.txt') as fh2:
    '''Opening assingent.txt as fh1 and new.txt as fh2'''
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)
        '''printing corresponding lines from both files'''

'''Q5'''
import random
'''importing random module'''

'''Opening num.txt in write mode'''
with open('num.txt','w') as fin:
    for i in range(1,11):
        '''Writing Random numbers in num.txt'''
        l = random.randint(0,999)
        fin.write(str(l) + "\n")
fin.close()
'''Closing num.txt'''
li = []
'''Opening num.txt in read mode'''
with open("num.txt","r") as fout:
    for line in fout:
        li.append(int(line))
        '''creating list from numbers in num.txt'''
    li.sort()
    '''Sorting the list'''
'''Opening sorted.txt in write mode'''
with open("sorted.txt", "w") as fsort:
    for i in range(0,10):
        fsort.write(str(li[i]) + "\n")
    '''Writing sorted numbers in sorted.txt'''
fout.close()
'''closing num.txt'''
fsort.close()
'''closing sorted.txt'''