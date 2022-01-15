"""  Student_ID : 20C073
    Student_Name: Dhwani Sakhiya
    Practical:2 (List,Tuple,Set,Dictionary) """

#DICTIONARY
# A)Write a Python script to check whether a given key already exists in a dictionary
dict={'red':'apple','blue':'sky','green':'trees','orange':'fire'}
print('The given dictionary : ',dict)
key="blue"
if key in dict:
    print(key,"is present")
else:
    print (key,"not present")

# B) Write a Python script to merge two Python dictionaries.
D1={'one':1,'two':2,'three':3,'four':4}
D2={'A':'apple','B':'ball','C':'cat','D':'doll'}
print('D1:',D1)
print('D2:',D2)
def Merge(D1,D2):
    xyz = D1|D2
    return xyz
D3=Merge(D1,D2)
print('D1+D2:' ,D3)

# C) Write a Python program to sum all the items in a dictionary.
Dict={'a': 350, 'b': 300, 'c': 250}
def returnSum(Dict):
    list = []
    for i in Dict:
        list.append(Dict[i])
    final = sum(list)

    return final
print('Dict:',Dict)
print("Sum of all the items in dict :", returnSum(Dict))

#D)Write a Python script to add a key to a dictionary
dict1={1:100,2:200,3:300}
dict1.update({4:400,5:500})
print('Dict1:',dict1)

#E)Write a Python script to concatenate following dictionaries to create a new one.
Dict1={1:10,2:20 }
Dict2 ={3:30,4:40 }
Dict3 ={5:50,6:60 }
print('Dict1: ',Dict1)
print('Dict2: ',Dict2)
print('Dict3: ',Dict3)
print('Dict1 + Dict2 + Dict3 :',Dict1|Dict2|Dict3)

#TUPLE
# A) Write a Python program to create a tuple with different data types.
tuple=('dhwani','i am good',True,50,63.0214)
print(tuple)

# B) Write a Python program to create a tuple with numbers and print one item.
tuple1 = 1, 11, 21, 31, 41,51
print('The given tupple is: ',tuple1)
tuple1 = 21
print('The one item from tupple is: ',tuple1)

# C) Write a Python program to add an item in a tuple.
tp=('red','yellow','orange','blue')
print('the given tupple is : ',tp)
a=("green")
tp = tp + (a,)
print('new tuple :',tp)

# D) Write a Python program to convert a tuple to a string.
tuple = ('d', 'h', 'w', 'a', 'n','i')
str =  ''.join(tuple)
print('the tupple is : ',tuple)
print('tuple created to string: ',str)


# E) Write a Python program to find the length of a tuple.
tuple2 = ("20cs073DhwaniSakhiya")
print('the tuple is: ',tuple2)
print('the length of the tuple is : ',len(tuple2))

#Set

# A) Write a Python program to add member(s) in a set and clear a set
numbers = {10,20,30,40}
print('the numbers are: ',numbers)
numbers.add(50)
print('new set of numbers are: ',numbers)

# B) Write a Python program to remove an item from a set if it is present in the set.
sets = set([30, 50, 76, 40, 54, 10])
print('the given set is : ',sets)
def Remove(sets):
    sets.discard(54)
    print('set after removing 54:',sets)
Remove(sets)

# C) Write a Python program to create an intersection, Union, difference of sets.
A = {10,30, 50, 70, 90};
B = {10, 20, 30, 40, 50};
print('Set A :',A)
print('Set B :',B)
# union
print("Union :", A | B)
# intersection
print("Intersection :", A & B)
# difference
print("Difference :", A - B)

# D) Write a Python program to find maximum and the minimum value in a set.
setA= set([88, 23, 30, 10, 25, 73, 10, 90, 52])
def MAX(sets):
    return (max(sets))
print('SetA: ',setA)
print('max value from setA: ',MAX(setA))
# Python code to get the minimum element from a set
setB = set([40, 15, 10, 92,9, 23])
def MIN(setB):
    return (min(setB))
print('SetB: ',setB)
print('max value from setB: ',MIN(setB))


# E) Write a Python program to find the most common elements and their counts from list, tuple, dictionary
print('LIST')
words=['yellow', 'green', 'blue', 'yellow','yellow','green']
print('list:',words)
from collections import Counter
c = Counter(words)
c.most_common(1)
print ('the most common element from the list :',c.most_common(1))

print('TUPLE')
words=('apple', 'grapes', 'cherry', 'grapes','cherry','orange')
print('tuple:',words)
from collections import Counter
c = Counter(words)
c.most_common(1)
print ('the most common element from the tuple :',c.most_common(1))

print('DICTIONARY')
word= { 'home','hospital','school','park','park'}
print('dict:',word)
from collections import Counter
c = Counter(word)
c.most_common(1)
print ('the most common element from the dict :',c.most_common(1))