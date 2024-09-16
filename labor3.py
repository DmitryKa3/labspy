import random
import string
list1 = []
list2 = []
for i in range(0,10):
    list1.append(random.choice(string.ascii_letters))
    list2.append(random.randint(0, 9))
print(list1,"\n",list2)
dictionary = {}

def function(lust1, list2):
    dictionary = {list1[i]:list2[i] for i in range(0,10)}
    return dictionary

dictionary = function(list1, list2)
print(dictionary)