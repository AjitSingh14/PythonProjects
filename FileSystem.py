import os

print (os.path.join('aaa','bbb','ccc'))
print(os.getcwd())
#os.makedirs('E:\\bbb\ccc\ddd')


print(os.getcwd().split(os.path.sep))
currentpath=os.getcwd()
print(currentpath)
print(os.path.getsize(currentpath))
print(os.listdir(currentpath))

totalsize=0

for filename in os.listdir(currentpath):
    if(os.path.exists(os.path.join(currentpath,filename))):
        print('FileName : ' + filename + ' Size : ' + str(os.path.getsize(os.path.join(currentpath,filename))) + ' bytes')
        totalsize+=os.path.getsize(os.path.join(currentpath,filename))
print('Total Size=' + str(totalsize))

ReadFile = open('E:\\aa\\ajit.txt')
print(ReadFile.readlines())
ReadFile.close()
AppendFile = open('E:\\aa\\ajit.txt','a')

AppendFile.write('\n Text from Program...')
AppendFile.close()


print( "%4.1f %s" % (33, 'ajit'))
