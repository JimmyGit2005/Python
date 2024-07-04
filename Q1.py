# Swapp First and Last Element of a list
list = [1,2,3,4,5]
for i in range(len(list)) :
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
print(list)
