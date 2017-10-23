#Task 4
x = 4
y = 10
z = ''

#We wrote an IF statement, that given two numerical variables x and y, swaps their values if x is less than y.
#We set the condition to be y greater than x.
#Given the condition to be true, we swapped the values by including a third variable, z, that allows us to move the values from x to z, from y to x and from z to y.
if x < y:
    z = x
    x = y
    y = z

print y
print x