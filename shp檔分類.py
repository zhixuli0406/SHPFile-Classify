import shapefile
import os
import shutil

SHP_PATH = 'D://前鎮小港公共管線圖資/前鎮小港公共管線圖資/管線圖資'
SHP_FORMAT = ['.shp']
SHP_SAVE_PATH = ['D://前鎮小港公共管線圖資/前鎮小港公共管線圖資/管線圖資/POINT','D://前鎮小港公共管線圖資/前鎮小港公共管線圖資/管線圖資/POLYLINE']
SHP_EXTENSION = ['.shp','.cpg','.dbf','.prj','.sbn','.sbx','.shx']
shp_name = [os.path.splitext(name)[0] for name in os.listdir(SHP_PATH) for item in SHP_FORMAT if os.path.splitext(name)[1] == item]

def Shp_Move():
    for x in range(0,len(shp_name)):
        sf = shapefile.Reader(SHP_PATH+'/'+shp_name[x])
        if sf.shapeType == shapefile.POINTZ :
            sf.close()
            for y in range(0,len(SHP_EXTENSION)):
                shutil.move(SHP_PATH+'/'+shp_name[x]+SHP_EXTENSION[y],SHP_SAVE_PATH[0]+'/'+shp_name[x]+SHP_EXTENSION[y])
        elif sf.shapeType == shapefile.POLYLINEZ :
            sf.close()
            for y in range(0,len(SHP_EXTENSION)):
                shutil.move(SHP_PATH+'/'+shp_name[x]+SHP_EXTENSION[y],SHP_SAVE_PATH[1]+'/'+shp_name[x]+SHP_EXTENSION[y])
    print("結束")
    return
Shp_Move()
