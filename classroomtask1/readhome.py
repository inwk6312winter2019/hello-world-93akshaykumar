import os

listfile=[]
listdir=[]

def readdir(path):
	global listfile,listdir
	for name in os.listdir(path):
		if os.path.isdir(path+'/'+name):
			listdir.append(name)
			readdir(path+'/'+name)
		elif os.path.isfile(path+'/'+name):
			listfile.append(name)
#walk('/home/akshaykumar')
print('The files present in home')
#readfile('/home/akshaykumar/akshaykumar')
readdir('/home')
print('THE LIST OF ALL THE FILES IN HOME AND SUB FOLDERS')
for item in listfile:
	print(listfile,sep="***",end="")
print()
print('THE LIST OF ALL THE DIRECTORIES IN HOME AND SUB DIRECTORIES IN REVERSE')
for item in listdir:
	print(item[::-1])
#print(os.listdir('/home'))
