import csv
with open("HW.csv",newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
# print(fileData[1:5])
fileData.pop(0)
heightList = []
for i in range(len(fileData)):
    height = fileData[i][1]
    heightList.append(float(height))

n = len(heightList)

sumheight = 0
for eachheight in heightList:
    sumheight = sumheight + eachheight

mean = sumheight/n

print(mean)
