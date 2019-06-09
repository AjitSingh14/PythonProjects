'''
This program is for generate the report of files and folder size of the root directories.
Author Name : Ajit Singh

- This will get the command argument of the 
                    root file which all file and folders size to be calculate
                    Report File Name and path

'''

import os, sys, csv
from importlib.resources import path

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            #return "%3.1f %s" % (num)
            return num, x    
        num /= 1024.0

def GetFileFolderSize(root, AllFilesSize, AllFoldersSize, count):
    
    currentDirSize=0
    
    try:
        allFilesAndFolders=os.listdir(root)
    except:
        allFilesAndFolders=[]
        print("Error accessing the file " + allFilesAndFolders)
    
    for name in allFilesAndFolders:
        path=os.path.join(root,name)
        
        if os.path.islink(path):
            print('This is link and skip ' + path)
        elif os.path.isfile(path):
            #print('Get the size of the file = ' + path)
            count[1]+=1
            filesize=os.path.getsize(path)
            AllFilesSize.append((path,filesize))
            currentDirSize+=filesize
        elif os.path.isdir(path):
            #print('Get the folder ' + path)
            count[0]+=1
            SubDirSize = GetFileFolderSize(path,AllFilesSize,AllFoldersSize,count)
            currentDirSize+=SubDirSize
        else:
            print("Error unknow file type " + path)
        
    AllFoldersSize.append((root, currentDirSize))
    return currentDirSize

def GenerateReport(AllFilesSize, AllFoldersSize, count):
    
    with open('My_Computer_Dir_File_Size.csv', mode='w',newline='') as My_Computer_Dir_File_Size:
        MyComWriter=csv.writer(My_Computer_Dir_File_Size, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        MyComWriter.writerow(['Directory Name', 'File Name', 'Size', 'Size Unit', 'is File', 'File Path'])
        
        for fileName, FileSizebyte in AllFilesSize:
            FileSize,FileSizeUnit  =convert_bytes(FileSizebyte)
            if (FileSizeUnit=='MB' and FileSize>10) or (FileSizeUnit=='GB'):
                MyComWriter.writerow(['', fileName.rsplit('\\',1)[1], round(FileSize), FileSizeUnit, 'Y', fileName])
            
        for FolderName, FolderSizebyte in AllFoldersSize:
            FolderSize, FolderSizeUnit =convert_bytes(FolderSizebyte)
            if (FolderSizeUnit=='MB' and FolderSize>10) or (FolderSizeUnit=='GB'):
                MyComWriter.writerow([FolderName.rsplit('\\',1)[1],'', round(FolderSize), FolderSizeUnit, 'N', FolderName])
        
        




if __name__ == '__main__':
    path="E:\\D Drive"
    AllFilesSize, AllFoldersSize=[],[]
    count=[0,1]
    SubDirSize = GetFileFolderSize(path,AllFilesSize,AllFoldersSize,count)
    print(AllFilesSize)
    print(AllFoldersSize)
    GenerateReport(AllFilesSize, AllFoldersSize, count)
    