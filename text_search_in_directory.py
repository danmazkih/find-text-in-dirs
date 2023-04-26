import os
import time


directory= r""

print(directory)
searchstring = input('What word are you trying to find? ')
starTime = time.time()
cont=0
for fname in os.listdir(directory):
    f = os.path.join(directory, fname)

    if os.path.isfile(f):
        # Full path
        f = open(f, 'r')

        if searchstring in f.read():
            cont+=1
            print('found string in file %s' % fname)
        
        f.close()
endTime = time.time()
TotalTime = endTime - starTime
print("Times Found: " + str(cont))
print("Elapsed execution time: " + str(TotalTime))

