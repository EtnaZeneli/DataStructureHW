count=1
file=open("TestFile.txt", "r")

for line in file.readlines():
    print(count, line)
    count= count +1
