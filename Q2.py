# Sawap two elements of given input
size = int(input("Enter Size of list : "))
list = []
for i in range(size) :
    list.append(int(input()))
print("Your Given List : ", list)
print("To swap number enter position index ")
pos1 = int(input("enter your first position : "))
pos2 = int(input("enter your second position : "))
for i in range(size) :
    temp = list[pos1] 
    list[pos1] = list[pos2]
    list[pos2] = temp
print("Your Final list output is : " , list)