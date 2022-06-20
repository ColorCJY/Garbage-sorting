# 对源数据集进行一些处理，成为自己的数据集
# 处理完后可以手动删除源数据集


import json
from move_file import *


def deal_file_name():
    path = "E:/Project/Python/Garbage/garbage_classify/raw_data"  # 源数据图片及其信息所在文件夹
    res_path = 'E:/Project/Python/Garbage/Data/train_val/main/train_val.txt'  # 保存图片文件名文件
    l1 = [set() for i in range(5)]  # 便于按文件最后的数字进行排序
    datas = os.listdir(path)  # 获取文件下的所有文件
    for i in datas:
        t = i[:-4]  # 删除后缀名.txt || .jpg
        l1[len(t) - 5].add(t)  # 长度一样的放在一起 img_1 || img_2 || img_10 || img_20 ...
    if os.path.exists(res_path):  # 因为是附加保存，为了不重复需要删除
        os.remove(res_path)  # 删除
    with open(res_path, 'a', encoding='UTF-8') as f:  # 保存
        for i in l1:  # 长度相同的依次排序保存
            t = list(i)  # set()->list才能排序
            t.sort()  # 排序
            for j in t:  # 逐个保存
                f.write(j + '\n')  # 一行一个文件


def deal_rule():
    path1 = "E:/Project/Python/Garbage/garbage_classify/garbage_classify_rule.json"  # 源数据集的分类信息
    res_path1 = "E:/Project/Python/Garbage/Data/classify_rule.json"  # 四分类规则
    res_path2 = "E:/Project/Python/Garbage/Data/train_classes.json"  # 多分类规则
    res1 = {}
    res2 = {}
    # 读取
    with open(path1, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    # 分割
    for i in data:
        s = data[i].split('/')
        if s[0] in res1:
            res1[s[0]].append(s[1])
        else:
            res1[s[0]] = [s[1]]
        res2[i] = s[1]
    # 显示与保存
    print(res1)
    print(res2)
    with open(res_path1, 'w', encoding='UTF-8') as f:
        json.dump(res1, f, indent=2)
    with open(res_path2, 'w', encoding='UTF-8') as f:
        json.dump(res2, f, indent=2)


def move_files():  # 移动文件
    old_path = r'E:/Project/Python/Garbage/garbage_classify/raw_data'  # 源文件所在位置
    new_path = r'E:/Project/Python/Garbage/Data/train_val/photo'  # 要将文件复制到的位置
    file_path = r'E:/Project/Python/Garbage/Data/train_val/main/train_val.txt'  # 保存了图片文件名的文件
    filename_lists = get_filename_from_txt(file_path, '.jpg')
    print(filename_lists)
    # 根据获取的信息进行遍历输出
    for filename in filename_lists:
        my_copy(old_path, new_path, filename)
    new_path = r'E:/Project/Python/Garbage/Data/train_val/message'  # 要将文件复制到的位置
    filename_lists = get_filename_from_txt(file_path, '.txt')
    print(filename_lists)
    # 根据获取的信息进行遍历输出
    for filename in filename_lists:
        my_copy(old_path, new_path, filename)  # 复制


if __name__ == '__main__':
    deal_file_name()
    deal_rule()
    # 可以不移动，用源数据集，但要注意其他程序文件中的一些处理会有更改
    # move_files()
