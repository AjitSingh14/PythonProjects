'''
Date - 24 Feb 2019
Chapter - File Systems and Handling
Topic - Compression
'''

import zipfile, os
ExampleZip=zipfile.ZipFile('Test.zip')

print(ExampleZip.namelist())

FileInfo= ExampleZip.getinfo('Test/TextFile.txt')
print('Original File Size - ' + str(FileInfo.file_size))
print('Compres Size - ' + str(FileInfo.compress_size))

ExampleZip.extract('Test/TextFile.txt','E:\\PythonProjects\\TestProject\\aa')

ExampleZip.close()