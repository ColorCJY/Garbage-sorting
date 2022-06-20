# 读取文件信息（文件名，信息，图片
from statistics_photo import *


photo_filenames = 'E:/Project/Python/Garbage/Data/train_val/main/'  # 含有图片名的文件
photo_messages = 'E:/Project/Python/Garbage/Data/train_val/message/'  # 图片类别信息文件所在位置
photo_place = 'E:/Project/Python/Garbage/Data/train_val/photo/'  # 图片所在位置
data_place = 'E:/Project/Python/Garbage/Data/'  # 一些数据文件所在位置


def get_json(file):  # 读取分类规则json文件
    """
    :param file: 读取的json文件名
    :return: 读出json中的字典
    """
    with open(data_place + file, 'r', encoding='UTF-8') as f:
        return json.load(f)


def read_filename(file):  # 读取文件文件名
    """
    :param file: 存储着文件名的文件的文件名
    :return: 文件名列表
    """
    # 各个图片的文件名是去除了后缀名一行放一个放在同一个文件里的
    with open(photo_filenames + file, 'r', encoding='UTF-8') as f1:
        file_name = f1.readlines()
    for i in range(len(file_name)):
        file_name[i] = file_name[i].strip('\n')
    return file_name


def read_message(file_name):  # 读取图片中的信息
    """
    :param file_name: 一个文件名
    :return: 分割好的文件名，类别
    """
    # txt文件中存储着是图片文件名和类别
    with open(photo_messages + file_name + '.txt', 'r', encoding='UTF-8') as f:
        s = f.readline().split(', ')
    return s  # s = [文件名, 类别]


def photo_class(file2, file3):  # 记录文件名对应的类型
    """
    :param file2: 用于存储文件名-垃圾类型的文件名
    :param file3: 存储着文件名的文件的文件名
    :return: 无
    """
    dit = {}
    file_name = read_filename(file3)  # 读取文件名
    n = len(file_name)  # 文件数量
    for i in range(n):  # 依次读取一个文件
        s = read_message(file_name[i])  # 读取图片中的信息
        dit[s[0]] = s[1]
    # 文件名-垃圾类型保存为文件
    with open(data_place + file2, 'w', encoding='utf-8') as f1:
        json.dump(dit, f1, indent=2)


def get_num(file1, file2, file3, p1, p2, title):  # 统计各种垃圾类别的数量
    """
    :param file1: 用于存储垃圾类型-数量信息的文件名
    :param file2: 用于存储文件名-垃圾类型的文件名
    :param file3: 存储着文件名的文件的文件名
    :param p1: 保存照片所在位置
    :param p2: 保存着存储垃圾类型-数量信息的文件文件位置
    :param title: 图片标题
    :return: 无
    """
    num = {}
    photo_class(file2, file3)
    kinds_name = get_json('train_classes.json')
    with open(data_place + file2, 'r', encoding='utf-8') as f1:
        dit = json.load(f1)  # 读取保存的文件名-垃圾类型信息
    for i in dit:
        if kinds_name[dit[i]] in num:
            num[kinds_name[dit[i]]] += 1
        else:
            num[kinds_name[dit[i]]] = 1
    with open(data_place + file1, 'w', encoding='utf-8') as f1:
        json.dump(num, f1, indent=2)
    draw_plt(p1, p2, title)
    print(num)  # 垃圾类型-数量信息
