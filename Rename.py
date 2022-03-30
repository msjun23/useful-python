import os

currDir = os.getcwd()

print("Folder name: ")
folderName = input()
path = currDir + '/' + folderName
#print(path)

print("Set file name: ")
fname = input()
# print(fname)

print("Set file format: ")
# print(fformat)
fformat = input()

cnt = 0
for f in os.listdir(path):
    #print(f)
    src = os.path.join(path, f)
    dst = fname + str(cnt) + '.' + fformat
    dst = os.path.join(path, dst)
    os.rename(src, dst)
    cnt += 1
