# 移动文件
# 需要先将所有要移动的文件的文件名(可以有后缀名/也可以没有)保存在一个txt文件中

import shutil
import os


# 从文件中获取要拷贝的文件的信息
def get_filename_from_txt(file, s):
    """
    :param file: 文件所在
    :param s: 提供的后缀名，为空表示保存文件中含有后缀名
    :return: 文件名列表
    """
    file_name_lists = []
    with open(file, 'r', encoding='utf-8') as f:
        lists = f.readlines()
        for one in lists:
            if s:
                file_name_lists.append(str(one).strip('\n') + s)  # 保存的文件名不含有后缀
            else:
                file_name_lists.append(str(one).strip('\n'))  # 保存的文件名含有后缀
    return file_name_lists


# 拷贝文件到新的文件夹中
def my_copy(src_path, dst_path, file_name):
    if not os.path.exists(src_path):
        print("src_path not exist!")
    if not os.path.exists(dst_path):
        print("dst_path not exist!")
    for root, dirs, files in os.walk(src_path, True):
        if file_name in files:
            # 如果存在就拷贝
            shutil.copy(os.path.join(root, file_name), dst_path)
        else:
            # 不存在的话将文件信息打印出来
            print(file_name)
