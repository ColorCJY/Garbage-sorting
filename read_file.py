# 读取文件信息（文件名，信息，图片）
from xml.dom import minidom  # 导入模块
import json

with open('E:/Project/Python/Data/test/classify_rule.json', 'r', encoding='UTF-8') as f:
    classify_rule = json.load(f)


def read_filename():  # 读取文件文件名
    with open(photo_filenames, 'r', encoding='UTF-8') as f1:
        file_name = f1.readlines()
    for i in range(len(file_name)):
        file_name[i] = file_name[i].strip('\n')
    return file_name


def read_message(file_name):  # 读取文件信息
    dom = minidom.parse(photo_messages + file_name + ".xml")  # 打开xml
    names = dom.getElementsByTagName("name")  # 获取节点列表
    l1 = []
    for i in range(len(names)):
        l1.append(names[i].firstChild.data)  # 打印节点数据
    return l1


def photo_class():  # 记录文件名对应的类型
    dit = {}
    file_name = read_filename()
    n = len(file_name)
    for i in range(n):
        # print(file_name[i])
        t = read_message(file_name[i])
        dit[file_name[i]+'.jpg'] = t[0]
    # with open('E:/Project/Python/Data/test/data.json', 'w', encoding='utf-8') as f1:
    #     json.dump(dit, f1, indent=2)
    #     if len(t) == 1:
    #         num += 1
    # print(num)


def get_num():  # 各种类别的数量
    num = {}
    with open('E:/Project/Python/Data/test/data.json', 'r', encoding='utf-8') as f1:
        dit = json.load(f1)
    print(dit)
    for i in dit:
        if dit[i] in num:
            num[dit[i]] += 1
        else:
            num[dit[i]] = 1
    # with open('E:/Project/Python/Data/test/data_num.json', 'w', encoding='utf-8') as f1:
    #     json.dump(num, f1, indent=2)


if __name__ == '__main__':
    photo_filenames = 'E:/Project/Python/Data/test/Main/trainval.txt'  # 文件名
    photo_messages = 'E:/Project/Python/Data/test/message/'  # 图片类别信息
    photo_place = 'E:/Project/Python/Data/test/photo/'  # 图片
    get_num()
