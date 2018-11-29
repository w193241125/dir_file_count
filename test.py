import os
import time

def list_dir(path, res):
    '''''
        res = {'dir':'root', 'child_dirs' : [] , 'files' : []}
        print list_dir('/root', res)
    '''
    for i in os.listdir(path):
        temp_dir = os.path.join(path, i)
        if os.path.isdir(temp_dir):
            temp = {'dir': temp_dir, 'child_dirs': [], 'files': []}
            res['child_dirs'].append(list_dir(temp_dir, temp))
        else:
            res['files'].append(i)
    return res


def get_config_dirs():
    res = {'dir': 'root', 'child_dirs': [], 'files': []}
    root = input('请输入目录:')
    return list_dir(root, res)


list = get_config_dirs()
first_dir = len(list['child_dirs'])
first_file = len(list['files'])
print('第一层目录下的目录有:', first_dir, '个')
print('第一层目录下的文件有:', first_file, '个')
for i in list['child_dirs']:
    sec_root = i['dir']
    sec_dir = len(i['child_dirs'])
    sec_file = len(i['files'])
    print(sec_root,' 目录下的目录有:', sec_dir, '个')
    print(sec_root,' 目录下的文件有:', sec_file, '个')
    if len(i['child_dirs'])>1:
        for j in i['child_dirs']:
            third_root = j['dir']
            third_dir = len(j['child_dirs'])
            third_file = len(j['files'])
            print(third_root, ' 目录下的目录有:', third_dir, '个')
            print(third_root, ' 目录下的文件有:', third_file, '个')

time.sleep(150)
