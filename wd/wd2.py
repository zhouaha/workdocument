import datetime
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
            f.write('time:'+str(datetime.datetime.now())+'\n')
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
                   'time:' + str(datetime.datetime.now())+ '\n',
                   'completionStatus:' + completionStatus + '\n',
                   '\n']
        data1 = data[0:(s-1)*6]
        for i in replace:
            data1.append(i)
        for i in data[s * 6:]:
            data1.append(i)
        print(data1)
        for i in data1:
            f_wd.write(i)

def select_todo():
    s = int(input('查询的id: '))
    with open('file.txt', encoding='utf-8',) as f:
        line = f.readlines()
        for i, rows in enumerate(line):
            if i in range((s-1)*6, s*6):
                print(rows)
        f.close()


def show_todo():
   print('****************************')
   print('*      选择输出排序的方式：    ')
   print('*      (默认优先级由高到底）   ')
   print('*1:优先级由低到高             ')
   print('*2:时间由高到低               ')
   print('*3:时间由低到高               ')
   print('*4:完成状态（todo,doing,done）')
   print('*5:完成状态（done,doing,todo）')
   print('****************************')
   s = int(input("选择排序方式："))
   with open('file.txt', 'r') as f:
        data = []
        data1 = []
        line = f.readlines()
        if s == 1:
            for i, rows in enumerate(line):
                if rows is '\n':
                    continue
            for i in range(int(len(line)/6)):
                data.append(line[6*i:6*i+6])
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
        elif s == 2:
            for i, rows in enumerate(line):
                if rows is '\n':
                    continue
            for i in range(int(len(line)/6)):
                data.append(line[6*i:6*i+6])
            print(data[0][3])
            print(data[1][3])
            if data[0][3] > data[1][3]:
                print('True')
        elif s == 3:
            pass
        elif s == 4:
            for i, rows in enumerate(line):
                if rows is '\n':
                    continue
            for i in range(int(len(line)/6)):
                data.append(line[6*i:6*i+6])
            for i in data:
                if i[4] == 'completionStatus:todo\n':
                    data1.append(i)
            for i in data:
                if i[4] == 'completionStatus:doing\n':
                    data1.append(i)
            for i in data:
                if i[4] == 'completionStatus:done\n':
                    data1.append(i)
            for i in data1:
                for j in i:
                    if f == '\n':
                        continue
                    print(j)
        elif s == 5:
            for i, rows in enumerate(line):
                if rows is '\n':
                    continue
            for i in range(int(len(line)/6)):
                data.append(line[6*i:6*i+6])
            for i in data:
                if i[4] == 'completionStatus:done\n':
                    data1.append(i)
            for i in data:
                if i[4] == 'completionStatus:todo\n':
                    data1.append(i)
            for i in data:
                if i[4] == 'completionStatus:doing\n':
                    data1.append(i)
            for i in data1:
                for j in i:
                    if f == '\n':
                        continue
                    print(j)
        else:
            for i, rows in enumerate(line):
                if rows is '\n':
                    continue
            for i in range(int(len(line)/6)):
                data.append(line[6*i:6*i+6])
            for i in data:
                if i[2] == 'priority:high\n':
                    data1.append(i)
            for i in data:
                if i[2] == 'priority:middle\n':
                    data1.append(i)
            for i in data:
                if i[2] == 'priority:low\n':
                    data1.append(i)
            for i in data1:
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



