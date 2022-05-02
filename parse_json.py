'''
parse images, get image id from image name, go through data['annotations'], put each image data in a txt file in new folder
'''
import json
import os
'''
imageDict = {}
jsonPath = 'instances_train2017.json'
f1 = open(jsonPath)
data = json.load(f1)
for i in data['annotations']:
    if i['image_id'] in imageDict.keys():
        newList = []
        newList.append(i['category_id'])
        newList.append(i['bbox'][0])
        newList.append(i['bbox'][1])
        newList.append(i['bbox'][2])
        newList.append(i['bbox'][3])
        imageDict[i['image_id']].append(newList)
    else:
        imageDict[i['image_id']] = []
        newList = []
        newList.append(i['category_id'])
        newList.append(i['bbox'][0])
        newList.append(i['bbox'][1])
        newList.append(i['bbox'][2])
        newList.append(i['bbox'][3])
        imageDict[i['image_id']].append(newList)

#print(imageDict)

dimDict = {}
for i in data['images']:
    if i['id'] not in dimDict.keys():
        list = []
        list.append(i['width'])
        list.append(i['height'])
        dimDict[i['id']] = list

#print(dimDict)


dirPath = 'C:/Users/anees/fiftyone/coco-2017/train/data/'

for file in os.listdir(dirPath):
    filename = os.fsdecode(file)
    pic_id = filename[:-4]
    pic_id = int(pic_id)

    txtPath = 'train/' + filename[:-4] + '.txt'
    f2 = open(txtPath, 'a')

    for i in imageDict[pic_id]:
        line = str(i[0] - 1) + " " + str((i[1] + i[3]) / (2 * dimDict[pic_id][0])) + " " + str(
            (i[2] + i[4]) / (2 * dimDict[pic_id][1])) + " " + \
               str(i[3] / dimDict[pic_id][0]) + " " + str(i[4] / dimDict[pic_id][1]) + "\n"
        f2.write(line)


'''
'''dirPath = 'C:/Users/anees/fiftyone/coco-2017/train/data/'

for file in os.listdir(dirPath):
    filename = os.fsdecode(file)
    pic_id = filename[:-4]
    pic_id = int(pic_id)

    jsonPath = 'instances_train2017.json'
    txtPath = 'train/' + filename[:-4] + '.txt'
    f1 = open(jsonPath)
    f2 = open(txtPath, 'a')
    data = json.load(f1)
    for i in data['annotations']:
        if i['image_id'] == pic_id:
            line = str(i['category_id']) + " " + str(i['bbox'][0]) + " " + str(i['bbox'][1]) + " " + \
                   str(i['bbox'][2]) + " " + str(i['bbox'][3]) + "\n"
            f2.write(line)
            
            '''



jsonPath = 'instances_train2017.json'
f1 = open(jsonPath)
data = json.load(f1)
keyList = []
for i in data['categories']:
    #keyList.append(i['name'])
    print(i['name'] + " " + str(i["id"]))
