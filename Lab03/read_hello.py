#Task 6
#We opened the file and for every line in it we printed the first four letters.
f = open('/Users/aliai/secu2002_master/data/hello_world.txt')
for line in f:
    print line[:4]
f.close()
