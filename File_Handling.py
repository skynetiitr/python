
f = open('File Handling.txt','r')
f1 = open('WriteFile.txt','w')
f1.write('This is File Write Example')
f1.write('\n')
f1.write('This is next line')
f1.write('\n')

for data in f:
    f1.write(data)

f1 = open('WriteFile.txt','r')
print(f1.read())
