import time
import re
import linecache

filename = 'file.txt'
def create_todo():
    #with open(filename,'w') as f:
     #   if f.read != None:
         #   print('**')
         #   f.write('\n')
    while True:
        with open(filename,'a') as f:
            id = input('输入ID：')
            name = input('输入name: ')
            priority = input('输入优先级(high,middle,low): ')
            completionStatus = input('输入完成状态(todo,doing,done): ')
            f.write('id:'+id +'\n')
            f.write('name:'+name +'\n')
            f.write('priority:'+priority +'\n')
            f.write('time:'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n')
            f.write('completionStatus:'+completionStatus +'\n')
            f.write('\n')
            i = input('继续输入y/n: ')
            if i == 'n':
                break

def delete_todo():
    s = int(input('删除的ID：'))
    with open('file.txt', 'r') as f:
        lines = f.readlines()
    with open('file.txt','w') as f_wd:
        for i, rows in enumerate(lines):
            if i in range((s - 1) * 6, s * 6):
                print(i,rows)
                continue
            f_wd.write(rows)

def update_todo():
    s = int(input('更改的ID：'))
    with open('file.txt', encoding='utf-8',) as f:
        line = f.readlines()
        for i, rows in enumerate(line):
            if i in range((s-1)*6, s*6):
                print(rows)
        f.close()
    name = input('输入更改name: ')
    priority = input('输入更改优先级(high,middle,low): ')
    completionStatus = input('输入更改完成状态(todo,doing,done): ')
    with open('file.txt', 'r') as f:
        lines = f.readlines()
    data = []
    with open('file.txt','w') as f_wd:
        for i, rows in enumerate(lines):
            data.append(rows)
        replace = ['id:' + str(s) + '\n',
                   'name:' + name + '\n',
                   'priority:' + priority + '\n',
                   'time:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+ '\n',
                   'completionStatus:' + completionStatus + '\n',
                   '\n']
        data1 = data[0:(s-1)*6]
        for i in replace:
            data1.append(i)
        for i in data[s * 6:]:
            data1.append(i)
        for i in data1:
            f_wd.write(i)

def select_todo():
    s = int(input('查询的id: '))
    data= []
    with open('file.txt', encoding='utf-8',) as f:
        line = f.readlines()
        for i, rows in enumerate(line):
            if i in range((s-1)*6, s*6):
                data.append(rows)
        for i, rows in enumerate(line):
            if i in range((s - 1) * 6, s * 6):
                print(rows)
        f.close()


def show_todo():
   print('****************************')
   print('*      选择输出排序的方式：    ')
   print('*1：升序                     ')
   print('*2：降序                     ')
   print('****************************')
   s = int(input('选择排序方式:'))
   with open('file.txt', 'r') as f:
       data = []
       data1 = []
       line = f.readlines()
   if s == 1:
       print('**************************')
       print('选择排序方式                ')
       print('1:优先级                   ')
       print('2:时间                     ')
       print('**************************')
       s1 = int(input('输入选项:'))
       if s1 == 1:
           for i, rows in enumerate(line):
               if rows is '\n':
                   continue
           for i in range(int(len(line) / 6)):
               data.append(line[6 * i:6 * i + 6])
           for i in data:
               if i[2] == 'priority:low\n':
                   data1.append(i)
           for i in data:
               if i[2] == 'priority:middle\n':
                   data1.append(i)
           for i in data:
               if i[2] == 'priority:high\n':
                   data1.append(i)
           for i in data1:
               for j in i:
                   if f == '\n':
                       continue
                   print(j)
       elif s1 == 2:
           for i, rows in enumerate(line):
               if rows is '\n':
                   continue
           for i in range(int(len(line) / 6)):
               data.append(line[6 * i:6 * i + 6])
           l = range(1,int(len(line) / 6))
           for i in l:
               print(data[i-1][3],data[i][3])
               if data[i-1][3] > data[i][3]:
                   data[i-1],data[i] = data[i],data[i-1]
               print(data)
           for i in data:
               for j in i:
                   if f == '\n':
                       continue
                   print(j)

   if s == 2:
       print('**************************')
       print('选择排序方式                ')
       print('1:优先级                   ')
       print('2:时间                     ')
       print('**************************')
       s1 = int(input('输入选项:'))
       if s1 == 1:
           for i, rows in enumerate(line):
               if rows is '\n':
                   continue
           for i in range(int(len(line) / 6)):
               data.append(line[6 * i:6 * i + 6])
           for i in data:
               if i[2] == 'priority:low\n':
                   data1.append(i)
           for i in data:
               if i[2] == 'priority:middle\n':
                   data1.append(i)
           for i in data:
               if i[2] == 'priority:high\n':
                   data1.append(i)
           for i in data1:
               for j in i:
                   if f == '\n':
                       continue
                   print(j)
       elif s1 == 2:
           for i, rows in enumerate(line):
               if rows is '\n':
                   continue
           for i in range(int(len(line) / 6)):
               data.append(line[6 * i:6 * i + 6])
           l = range(1,int(len(line) / 6))
           for i in l:
               print(data[i-1][3],data[i][3])
               if data[i-1][3] < data[i][3]:
                   data[i-1],data[i] = data[i],data[i-1]
               print(data)
           for i in data:
               for j in i:
                   if f == '\n':
                       continue
                   print(j)

if __name__ == '__main__':
    while True:
        print('****************')
        print('*1:创建todo     ')
        print('*2:删除todo     ')
        print('*3:更改todo     ')
        print('*4:查询todo     ')
        print('*5:列出列表      ')
        print('****************')
        i = int(input('输入操作选项：'))
        if i == 1:
            create_todo()
            continue
        elif i == 2:
            delete_todo()
            continue
        elif i == 3:
            update_todo()
            continue
        elif i == 4:
            select_todo()
            continue
        elif i == 5:
            show_todo()
            continue
        else:
            break



