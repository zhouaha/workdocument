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
            f.write('time:'+time.strftime('%Y.%m.%d',time.localtime(time.time()))+'\n')
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
    id = input('输入更改ID：')
    name = input('输入更改name: ')
    priority = input('输入更改优先级(high,middle,low): ')
    completionStatus = input('输入更改完成状态(todo,doing,done): ')
    with open('file.txt', 'r') as f:
        lines = f.readlines()
    with open('file.txt','w') as f_wd:
        for i, rows in enumerate(lines):
            if i in range((s - 1) * 6, s * 6):
                print(i,rows)
                f.write('id:' + id + '\n')
                f.write('name:' + name + '\n')
                f.write('priority:' + priority + '\n')
                f.write('time:' + time.strftime('%Y.%m.%d', time.localtime(time.time())) + '\n')
                f.write('completionStatus:' + completionStatus + '\n')
            f_wd.write(rows)


def select_todo():
    s = int(input('查询的id: '))
    with open('file.txt', encoding='utf-8',) as f:
        line = f.readlines()
        for i, rows in enumerate(line):
            if i in range((s-1)*6, s*6):
                print(rows)
        f.close()


def show_todo():
    data = []
    with open('file.txt', encoding='utf-8',) as txtfile:
        line = txtfile.readlines()
        for i, rows in enumerate(line):
            if i in range(5158, len(line)):
                print(rows)
                data.append(rows)
    print("length",len(data))
    txtfile.close()


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



