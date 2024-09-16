import random
list1 = []
print("Введите n")
n = int(input())
for i in range(0,n):
    list1.append(random.randint(0,9))
list2 = []

def function (list):
    for i in range(0,len(list)):
        if list[i]*list[i] < 30:
            list2.append(list[i])

print(list1)
function(list1)
print(list2)