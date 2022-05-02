import os

dirPath = 'labels2/'

for file in os.listdir(dirPath):
    filename = os.fsdecode(file)
    path1 = dirPath + filename
    path2 = 'coco128/newLabels/' + filename

    f1 = open(path1, 'r')
    f2 = open(path2, 'w')

    for item in f1:
        lineSplit = item.split(' ')
        f2.write(item.replace(lineSplit[0], str(int(lineSplit[0]) + 80)))
