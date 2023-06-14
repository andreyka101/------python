file = open('24k.txt')
fileData = ''
mxstr = 1
s=1
for i in file:
    fileData += i
for i in range(len(fileData)-1):
    if fileData[i] == "X" and fileData[i+1] == "X":
        s+=1
        mxstr = max(mxstr,s)
    else:
        s=1
print (mxstr)