# DHWANI SAKHIYA (20CS073)

# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

#for list:
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

#for tuple
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))