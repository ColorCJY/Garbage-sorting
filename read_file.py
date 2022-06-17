# 读取文件信息（文件名，信息，图片）
from xml.dom import minidom  # 导入模块
import json


def get_classify_rule():  # 读取分类规则
    with open(class_rule, 'r', encoding='UTF-8') as f:
        return json.load(f)


def read_filename():  # 读取文件文件名
    # 各个图片的文件名是去除了后缀名一行放一个放在同一个文件里的
    with open(photo_filenames, 'r', encoding='UTF-8') as f1:
        file_name = f1.readlines()
    for i in range(len(file_name)):
        file_name[i] = file_name[i].strip('\n')
    return file_name


def read_message(file_name):  # 读取图片中的信息
    # xml文件中存储着是图片的信息
    dom = minidom.parse(photo_messages + file_name + ".xml")  # 打开xml
    names = dom.getElementsByTagName("name")  # 获取节点列表
    l1 = []
    for i in range(len(names)):
        l1.append(names[i].firstChild.data)  # 打印节点数据
    return l1


def photo_class():  # 记录文件名对应的类型
    dit = {}
    num = 0  # 统计数量
    file_name = read_filename()  # 读取文件名
    n = len(file_name)  # 文件数量
    for i in range(n):  # 依次读取一个文件
        print(file_name[i])  # 显示当前文件
        t = read_message(file_name[i])  # 读取图片中的信息
        if len(t) == 1:
            dit[file_name[i] + '.jpg'] = t[0]
            num += 1
    # 文件名-垃圾类型保存为文件
    # with open(data_place + 'data.json', 'w', encoding='utf-8') as f1:
    #     json.dump(dit, f1, indent=2)
    # print(num)  # 显示数量


def get_num():  # 统计各种垃圾类别的数量
    num = {}
    with open(data_place + 'data.json', 'r', encoding='utf-8') as f1:
        dit = json.load(f1)  # 读取保存的文件名-垃圾类型信息
    print(dit)  # 显示文件名-类型信息
    for i in dit:
        if dit[i] in num:
            num[dit[i]] += 1
        else:
            num[dit[i]] = 1
    # with open(data_place + 'data_num.json', 'w', encoding='utf-8') as f1:
    #     json.dump(num, f1, indent=2)
    print(num)  # 垃圾类型-数量信息


if __name__ == '__main__':
    photo_filenames = 'E:/Project/Python/Garbage/Data/test/Main/train_val.txt'  # 含有图片名的文件
    photo_messages = 'E:/Project/Python/Garbage/Data/test/message/'  # 图片类别信息文件所在位置
    photo_place = 'E:/Project/Python/Garbage/Data/test/photo/'  # 图片所在位置
    data_place = 'E:/Project/Python/Garbage/Data/test/'  # 数据文件所在位置
    class_rule = 'E:/Project/Python/Garbage/Data/test/classify_rule.json'  # 分类规则位置
    get_num()
