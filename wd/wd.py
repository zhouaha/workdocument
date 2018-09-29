import time
import re
import linecache

filename = 'file.txt'
def createtodo():
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
            json = {'ID':id,
                    'name': name,
                    'priority': priority,
                    'time': time.strftime('%Y.%m.%d',time.localtime(time.time())),
                    'completionStatus': completionStatus}
            f.write(str(json)+'\n')
            f.write('\n')
            i = input('继续输入y/n: ')
            if i == 'n':
                break

def deletetodo():
    s = int(input('删除的ID：'))
    count = linecache.getline('file.txt', s*2-1)
    print(count)
    with open('file.txt', 'r') as f:
        lines = f.readlines()
    with open('file.txt', 'w') as f_wd:
        for line in lines:
            if count in line:
                continue
            f_wd.write(line)


def updatetodo():
    #count = len(open('file.txt', 'rU').readlines())
    s = int(input('更改的id: '))

    count = linecache.getline('file.txt', (s - 1) * 2 + 1)
    print(count)
    name = input('输入name: ')
    priority = input('输入优先级(high,middle,low): ')
    completionStatus = input('输入完成状态(todo,doing,done): ')


def selecttodo():
    s = int(input('查询的id: '))
    count = linecache.getline('file.txt',s*2-1)
    print(count)

def showtodo():
    with open('file.txt','r') as f:
        lines = f.readlines()
        L1 = []
        L2 = []
        L3 = []
        for line in lines:
            if line != '\n':
                id = eval(line).get('ID')
                priority = eval(line).get('priority')
                if priority =='high':
                    L1.append(int(id))
                elif priority == 'middle':
                    L2.append(int(id))
                elif priority == 'low':
                    L3.append(int(id))
        for s in L1:
            count = linecache.getline('file.txt', s * 2 - 1)
            print(count)
        for s in L2:
            count = linecache.getline('file.txt', s * 2 - 1)
            print(count)
        for s in L3:
            count = linecache.getline('file.txt', s * 2 - 1)
            print(count)


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
            createtodo()
            continue
        elif i == 2:
            deletetodo()
            continue
        elif i == 3:
            updatetodo()
            continue
        elif i == 4:
            selecttodo()
            continue
        elif i == 5:
            showtodo()
            continue
        else:
            break



