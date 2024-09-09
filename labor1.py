import random
list1 = []
for i in range(0,3):
    list1.append(random.randint(0,9))

def function (list1):
    if list1[0] > list1[2]:
        list1[1] = list1[0]
        list1[2] = list1[0]
    else:
        list1[0] = list1[2]
        list1[1] = list1[2]
print(list1)
function(list1)
print(list1)