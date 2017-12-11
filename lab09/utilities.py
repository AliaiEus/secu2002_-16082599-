# TASK 1
# The following represents a linear search algorithm that iterates through the list until it finds the element it wants.

# Open a list of integers data
data = [1, 2, 3, 4, 5, 7, 9, 10, 13, 15, 16, 19, 20]
# Define the integer element e to be found in the list
e = 5

# Define a function lin_find that, given an integer e and a list of integers data, uses a for loop to find and return that entry in the list, if it is there.
def lin_find (mylist, integer):
    # Set the variable count a to zero
    count_loop = 0
    # The for loop iterates over the sequence data and once the integer is found, the process stops and the result is printed
    for i in mylist:
        count_loop += 1
        if i == integer:
            print integer
            break
    print 'Number of times with linear search is', count_loop

lin_find(data, e)

# TASK 2
# The following represents a binar search algorithm that iterates through the list until it finds the element it wants.

# Define a function bin_find that, given an integer e and a list of integers data, uses a for loop to find and return that entry in the list, if it is there.
def bin_find (mylist, integer):
    # Set the variable first to zero indicating that I am starting at the beginning of the list
    first = 0
    # Set the variable last to len(mylist)-1 indicating that I am ending at the end of the list
    last = len(mylist)-1
    # Set the variable count a to zero
    bin_count = 0
    # I want to consider the whole list
    while last>first:
        bin_count += 1
        # I pick as a pivot the element at the midpoint of the list; i.e., the element at index (first + last) / 2
        pivot = (first + last) / 2
        # 1step:
        if mylist[pivot] < integer:
            # Update first to be one more than the index of the pivot element
            first = pivot + 1
        elif mylist[pivot] > integer:
            # Update last element to be one less than the index of the pivot element
            last = pivot - 1
        elif mylist[pivot] == integer:
            print 'The integer', integer, 'goes through the loop', bin_count, 'number of times'
            break
        else:
            print 'The integer chosen is not in the list'

bin_find(data, e)