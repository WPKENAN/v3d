import os



if __name__=="__main__":
    apoFolder = "/home/liyading/PBserver/wpkenan/10000/apo";
    resultFolder = "/home/liyading/PBserver/wpkenan/10000/result"

    apoFileDict = {}
    for file in os.listdir(apoFolder):
        if file.split('.')[-1] == 'apo':
            # apoFileList.append(os.path.join(apoFolder,file));
            apoFileDict[file.split('_')[0]] = os.path.join(apoFolder, file)

    count=0;
    for brainId in apoFileDict.keys():
        path=os.path.join(resultFolder,brainId,"out")
        count+=len(os.listdir(path))
    print(count)

