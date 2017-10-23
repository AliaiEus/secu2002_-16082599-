#Task 7
#We created a file - hello_world.txt - and filled it with the content "Hello World!).
# 'w' allows us to immediately erase the contents of the file, if it exists.
f = open('hello_world.txt', 'w')
f.write('Hello World!')
f.close()



