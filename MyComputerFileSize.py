# Import the os module, for the os.walk function
import os
import csv

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            #return "%3.1f %s" % (num)
            return num, x    
        num /= 1024.0

# Set the directory you want to start from
rootDir = 'E:\\aa'
with open('My_Computer_Dir_File_Size.csv', mode='w',newline='') as My_Computer_Dir_File_Size:
    MyComWriter=csv.writer(My_Computer_Dir_File_Size, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    MyComWriter.writerow(['Directory Name', 'File Name', 'Size', 'Size Unit', 'is File', 'File Path'])

    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        total_size = 0
        
        for fname in fileList:
            FileSize=''
            FileSizeUnit=''
            fp=os.path.join(dirName,fname)
            total_size += os.path.getsize(fp)
            FileSizeUnit, FileSize =convert_bytes(os.path.getsize(fp))
            MyComWriter.writerow([dirName, fname, FileSize, FileSizeUnit, 'Y', fp])
            print('\t%s' % fname)
        FolderSizeUnit, FolderSize =convert_bytes(total_size)
        MyComWriter.writerow([dirName, '', FolderSize,FolderSizeUnit , 'N', dirName])

