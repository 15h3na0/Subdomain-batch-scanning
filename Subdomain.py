"""
@Author : 15h3na0
@Time : 2020/4/3 14:57
@Blog: https://15h3na0.xyz/
"""
import os
import sys
import threading

url = []
SepList = []


def read_file(file_path):
    # 判断文件路径是否存在，如果存在则读取文件内容，否则直接退出。
    if not os.path.exists(file_path):
        print('Filepath error !!!')
        sys.exit(0)
    else:
        with open(file_path, 'r') as source:
            for line in source:
                url.append(line.rstrip('\r\n').rstrip('\n'))


# 分离函数
def separatename(threadcount):
    for i in range(0, len(url), int(len(url) / threadcount)):
        SepList.append(url[i:i + int(len(url) / threadcount)])


# 多线程函数
def multithreading(threadcount):
    separatename(threadcount)
    for i in range(threadcount):
        t = threading.Thread(target=onethread, args=(SepList[i],))
        t.start()


# 每个线程的函数
def onethread(url):
    for i, j in zip(url, range(len(url))):
        str = ('python3 oneforall.py --target {0} run')
        str = str.format(url[j])
        print(str)
        os.system(str)


if __name__ == '__main__':
    file_str = 'url.txt'
    read_file(file_str)
    # 设定线程
    thread_num = 3
    multithreading(thread_num)
