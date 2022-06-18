# 利用pytorch进行随机分割训练集:测试集 = 8:2
import torch


def get_file():  # 获取数据集的文件名
    file_names = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        file_list = f.readlines()
    for i in file_list:
        file_names.append(i.strip('\n'))
    return file_names


def divide_file():
    file_names = get_file()  # 获取到的数据集文件名列表
    train_size = int(0.8 * len(file_names))  # 训练集的大小
    test_size = len(file_names) - train_size  # 测试集的大小
    train_set, test_set = torch.utils.data.random_split(file_names, [train_size, test_size])  # 随机划分train:test = 8:2
    # 转换为列表
    train_set = list(train_set)
    test_set = list(test_set)
    # 加上后缀名保存至文件
    with open(result_path + 'train_set.txt', 'w', encoding='UTF-8') as f:
        for i in train_set:
            f.write(i + '.jpg\n')
    with open(result_path + 'test_set.txt', 'w', encoding='UTF-8') as f:
        for i in test_set:
            f.write(i + '.jpg\n')


if __name__ == '__main__':
    file_name = 'E:/Project/Python/Garbage/Data/test/main/train_val.txt'  # 保存着数据集的文件名
    result_path = 'E:/Project/Python/Garbage/Data/test/main/'  # 结果保存的地方
    divide_file()
