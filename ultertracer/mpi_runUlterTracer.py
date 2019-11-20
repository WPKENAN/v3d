import os
import sys
import multiprocessing
import time

def ulterTracer(brainPath,markerPath,outPath,brainId,vaa3dPath,id):
    commandStr='sh /home/braincenter12/PBserver/wpkenan/10000/mutil_batch_auto_tracing-app2.sh \'{}\' \'{}\' \'{}\' \'{}\' {} {}'\
        .format(brainPath,markerPath,outPath,vaa3dPath,brainId,id)


    print(commandStr)
    os.system(commandStr)


def apo2Marker(path):
    apo=open(path).readlines()

    markerTitle = '##x,y,z,radius,shape,name,comment, color_r,color_g,color_b\n'

    marker=open(path.strip('.apo')+".marker",'w')
    marker.write(markerTitle)
    for i in range(1,len(apo)):
        line=apo[i].strip('\n').split(',')
        # print(line)
        # print("{}, {}, {}, {},{},{},{},{},{},{}\n".
        #              format(line[5],line[6],line[4],0,0,line[2],' ',line[-3],line[-2],line[-1]))
        marker.write("{}, {}, {}, {},{},{},{},{},{},{}\n".
                     format(line[5],line[6],line[4],0,0,line[2],' ',line[-3],line[-2],line[-1]))

    marker.close()




def splitMarkers(path, outfolder,scale=2):
    file = open(path)
    content = file.readlines()
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)
    count = 10000;
    for i in range(1, len(content)):
        line = content[i].strip('\n').split(',');
        # print(line, '***', line[-1])
        # if int(line[-1])==255 and int(line[-2])==100 and int(line[-3])==1:
        #	continue;

        try:
            out = open(os.path.join(outfolder,
                                    '{}_{}_{}_{}.v3draw.marker'.format(int(line[5]), float(line[0]), float(line[1]),
                                                                       float(line[2]))), 'w')
            out.write(content[0])
            out.write(
                '{},{},{},{},{},{},{},{},{},{}\n'.format(float(line[0]) / scale, float(line[1]) / scale, float(line[2]) / scale,
                                                         line[3], line[4], line[5], line[6], line[7], line[8], line[9]))
        except:
            out = open(os.path.join(outfolder, '{}_{}_{}_{}.v3draw.marker'.format(count, float(line[0]), float(line[1]),
                                                                                  float(line[2]))), 'w')
            out.write(content[0])
            out.write(
                '{},{},{},{},{},{},{},{},{},{}\n'.format(float(line[0]) / scale, float(line[1]) / scale, float(line[2]) / scale,
                                                         line[3], line[4], count, line[6], line[7], line[8], line[9]))
            count = count + 1
        out.close()






if __name__=="__main__":
    apoFolder="/home/liyading/PBserver/wpkenan/10000/apo";
    resultFolder="/home/liyading/PBserver/wpkenan/10000/result"


    if not os.path.exists(resultFolder):
        os.mkdir(resultFolder)


    print("start split apo")
    apoFileDict={}
    for file in os.listdir(apoFolder):
        if file.split('.')[-1]=='apo':
            # apoFileList.append(os.path.join(apoFolder,file));
            apoFileDict[file.split('_')[0]]=os.path.join(apoFolder,file)
            if not os.path.exists(os.path.join(resultFolder,file.split('_')[0])):
                # print(os.path.join(resultFolder,file.split('_')[0]))
                os.mkdir(os.path.join(resultFolder,file.split('_')[0]))



    #apo2Marker
    print("start apo2Marker")
    for brainId in apoFileDict.keys():
        apo2Marker(apoFileDict[brainId])


    print("start split marker")

    cores=multiprocessing.cpu_count()
    cores=10
    pool=multiprocessing.Pool(processes=cores)
    start=time.time()
    #splitMarkers
    for brainId in apoFileDict.keys():
        print(brainId)
        if not os.path.exists(os.path.join(resultFolder,brainId,'out')):
            os.mkdir(os.path.join(resultFolder,brainId,'out'))
        # print(brainId)
        # # apo2Marker(apoFileDict[brainId])
        pool.apply_async(splitMarkers,(apoFileDict[brainId].strip('.apo')+".marker",os.path.join(resultFolder,brainId,"marker"),2))
        # path=
        # splitMarkers(path,os.path.join(resultFolder,brainId),2)
    pool.close()
    pool.join()
    end=time.time()
    print(time.time()-start)

    brainFolder='/home/braincenter12/PBserver/TeraconvertedBrain'
    brainFileDict={}
    for brainId in apoFileDict.keys():
        for brainFile in os.listdir(brainFolder):
            if brainId in brainFile:


                tmp1=os.listdir(os.path.join(brainFolder,brainFile))

                # tmp.remove('vmap.bin')
                tmp=[]


                for res in tmp1:
                    if 'RES(' in res:
                        tmp.append(res)
                # print(tmp)
                # print(tmp[0])
                # print(tmp[0].split['('][-1].split('x')[0])
                tmp.sort(key=lambda x:int(x.split('(')[-1].split('x')[0]))
                print(tmp)
                brainFileDict[brainId]=os.path.join(brainFolder,brainFile,tmp[-2])



    print(brainFileDict)

    cores=multiprocessing.cpu_count()
    cores=10
    pool=multiprocessing.Pool(processes=cores)
    start = time.time()

    for brainId in apoFileDict.keys():
        for markerPath in os.listdir(os.path.join(resultFolder,brainId,'marker')):
    #
    #
    #
            # brainPath, markerPath, outPath, brainId, vaa3dPath=brainFileDict[brainId],\
            #                                                    os.path.join(resultFolder,brainId,'marker',markerPath),\
            #                                                    os.path.join(resultFolder,brainId,'out'),\
            #                                                    '/home/braincenter12/v3d_external/bin',\
            #                                                    brainId
            # print()

            # ulterTracer(brainPath, markerPath, outPath, brainId, vaa3dPath)
            pool.apply_async(ulterTracer,
                             (brainFileDict[brainId],
                              os.path.join(resultFolder,brainId,'marker',markerPath),
                              os.path.join(resultFolder,brainId,'out'),
                              brainId,
                              '/home/braincenter12/v3d_external/bin',markerPath[0:4]))

    pool.close()
    pool.join()
    end=time.time()
    print(time.time()-start)




















