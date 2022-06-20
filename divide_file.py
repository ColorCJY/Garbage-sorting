# 利用pytorch进行随机分割训练集:测试集 = 8:2
import torch
from read_file import *


def get_file():  # 获取数据集的文件名
    file_names = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        file_list = f.readlines()
    for i in file_list:
        file_names.append(i.strip('\n'))
    return file_names


def divide_file():  # 分割数据集
    file_names = get_file()  # 获取到的数据集文件名列表
    train_size = int(0.8 * len(file_names))  # 训练集的大小
    test_size = len(file_names) - train_size  # 测试集的大小
    train_set, test_set = torch.utils.data.random_split(file_names, [train_size, test_size])  # 随机划分train:test = 8:2
    # 转换为列表
    train_set = list(train_set)
    test_set = list(test_set)
    # 保存文件以及数量显示
    # 训练集
    p_1 = 'E:/Project/Python/Garbage/Data/statistics_train.jpg'
    p_2 = 'E:/Project/Python/Garbage/Data/train_num.json'
    with open(result_path + 'train_set.txt', 'w', encoding='UTF-8') as f:
        for i in train_set:
            f.write(i + '\n')
    get_num("train_num.json", "train_kinds.json", "train_set.txt", p_1, p_2, '训练集情况')
    # 测试集
    p_1 = 'E:/Project/Python/Garbage/Data/statistics_test.jpg'
    p_2 = 'E:/Project/Python/Garbage/Data/test_num.json'
    with open(result_path + 'test_set.txt', 'w', encoding='UTF-8') as f:
        for i in test_set:
            f.write(i + '\n')
    get_num("test_num.json", "test_kinds.json", "test_set.txt", p_1, p_2, '测试集情况')


if __name__ == '__main__':
    # 先进行总体数据信息的整理
    path1 = 'E:/Project/Python/Garbage/Data/statistics_result.jpg'
    path2 = 'E:/Project/Python/Garbage/Data/kinds_num.json'
    get_num("kinds_num.json", "file_kinds.json", "train_val.txt", path1, path2, '数据集情况')
    # 分割数据集
    file_name = 'E:/Project/Python/Garbage/Data/train_val/main/train_val.txt'  # 保存着数据集的文件名
    result_path = 'E:/Project/Python/Garbage/Data/train_val/main/'  # 结果保存的地方
    divide_file()
