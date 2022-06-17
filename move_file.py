# 移动文件

import shutil
import os

old_path = r'E:/Project/Python/Garbage/Data/train_val_0629/VOC2007/Annotations'  # 源文件所在位置
new_path = r'E:/Project/Python/Garbage/Data/test/message'  # 要将文件复制到的位置
file_path = r'E:/Project/Python/Garbage/Data/train_val.txt'  # 保存了图片文件名的文件


# 从文件中获取要拷贝的文件的信息
def get_filename_from_txt(file):
    file_name_lists = []
    with open(file, 'r', encoding='utf-8') as f:
        lists = f.readlines()
        for one in lists:
            file_name_lists.append(str(one).strip('\n'))
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


if __name__ == "__main__":
    # 执行获取文件信息的程序
    filename_lists = get_filename_from_txt(file_path)
    print(filename_lists)
    # 根据获取的信息进行遍历输出
    for filename in filename_lists:
        my_copy(old_path, new_path, filename)
