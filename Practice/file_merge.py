from datetime import datetime
from glob import glob
file1=open('example.txt','r')
file2=open('example_w.txt','r')
file3=open('example.txt','r')

with open(datetime.now().strftime('%Y')+'.txt','w+') as merge_file:
    merge_file.write(file1.read())
    merge_file.write(file2.read())
    merge_file.write(file3.read())
    merge_file.close()