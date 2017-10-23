#Task 5
#We mimic the bahaviour of a for loop by writing a while loop that goes through the following numeric list and print x+1 for every x in the list:
mylist = [7, 13, 24, 5]
#We assigned the value of zero to the index variable.
#We started at the first element (0th) in mylist and then retrieve each item in the list order, until the end of the list defined by measuring its lenght.
#The while loop ends as the statement then becomes false; because the lenght of the list has no more that four values, thus the while loop ceases.
i = 0
while i < len(mylist):
    #The index method we used allows us to finds the given element in a list and returns its position.
    #We printed i (index variable) + 1 for every element in the list.
    print mylist[i]+1
    i += 1

