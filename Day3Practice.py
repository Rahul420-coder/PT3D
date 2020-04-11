"""
#loops

1. while
2. For each
"""

number = 0

while (number < 10):
    number = number + 1
    if number == 5:
        break
    print (number)
    
number = 0

while (number < 10):
    number = number + 1
    if number == 5:
        continue
    print (number)
    
    
    
#list

list1 = []
type(list1)

list1 = [1,2,4,10, 56, 10]
len(list1)



list1[0]
list1[-1]


list1[0:4]

list1.index(10)


list1[0] = 100
print (list1)




list1 = [1,2,4,10, 56, 10]

for x in list1:
    print (x)


list1 = [10,3,12,15]
list1.append(100)
print (list1)

list1.insert(1, 102)
print (list1)


list1.clear()
print (list1)

list1 = [10,3,12,15]
list1.remove(12)

print (list1)


list2 = [100, 200, 300]
    
list3 = list1 + list2

list1.extend(list2)

print (list1)
list1.pop()
list1.pop()

list1.pop(0)



list1 = [10,3,12,15]
list1.sort(reverse = True)
print(list1)



#list are hetrogenious

list1 = [10, 'India', True, 3.4]



list1 = [10, 20, 3, 20, 13, 20]

list1.count(20)
list1.remove(20)
list1.remove(20)
list1.remove(20)

list1 = [10, 20, 3, 20, 13, 20]

while 20 in list1:
    list1.remove(20)

    


#functions
#in built functions



def addvalues(a, b):
    """
    Doc string
    This functions adds two values
    
    """
    return (a+b)


addvalues(10, 12)


list1 = [1,2,3,4]

list2 = [10,11,12,13]

list1.extend(list2)

list1 = list1+list2

#loops
while - for indefinite iterations
for - definite iterations

list1 = [1,2,3,4]

for item in list1[0:3]:
    print (item)


list1 = [[1,2,3],[10,20,30]]

list1 = [10, 'Ram', 2.3]

type(list1[2])

list1  = [1,2,3,4,5,6]
list1.pop()

list1[0:4]
list1[:]

list1[::2]

list1[::-1]



list1 = input("Enter your name:").split()


while True:
    print ("Hello")


list1 = [1,2,3,4,5]

del (list1)


list1 = [1,2,3,4,5]
list1.clear()



