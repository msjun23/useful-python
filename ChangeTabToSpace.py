import os

currDir = os.getcwd()

path = currDir

print("Set file name: ")
print("ex) test.txt")
fname = input()
path = currDir
print(path)

f = open(path + '\\' + fname, 'r')
body = f.read()
f.close()

body = body.replace('\t', ' ')

print("Set new file nema: ")
print("ex) new_test.txt")
nfname = input()
nf = open(path + '\\' + nfname, 'w')
nf.write(body)
nf.close()
