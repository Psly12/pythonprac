'''
This script creates a txt files and adds number of lines passed as argument
'''
from datetime import datetime

def add_lines_to_files(num_of_lines):
    '''This function creates a txt files and adds number of lines passed as argument'''
    file_a=open(datetime.now().strftime('%Y-%m-%d'),'a+')
    file_a.seek(0)
    lines=file_a.readlines()
    file_a.seek(2)
    print(lines)
    if len(lines)>0:
        line_num=[int(wrd) for wrd in lines[-1].split() if wrd.isdigit()]
        print(line_num)
        if len(line_num)>0:
            for i in range(line_num[-1]+1,line_num[-1]+num_of_lines+1):
                file_a.write('Line {}\n'.format(i))
        else:
            print("Could not finr the Line number.")
    else:
        for i in range(1,num_of_lines+1):
            file_a.write('Line {}\n'.format(i))
    file_a.close()

add_lines_to_files(int(input('Enter the number of lines you want to add : ')))

'''
file = open("example.txt",'r')
print(file.read())
file.seek(0)
lines=file.readlines()
lines = [len(l.rstrip("\n")) for l in lines]
print(lines) 
'''