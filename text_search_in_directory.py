import os
import time


directory= r"C:\Users\BECING3_22\Desktop\logs"

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
print("Veces encontradas: " + str(cont))
print("Tiempo transcurrido de ejecución: " + str(TotalTime))

