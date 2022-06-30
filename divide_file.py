# 利用pytorch进行随机分割训练集:测试集 = 8:2
import shutil
import sys
import torch
from tqdm import tqdm
from read_file import *
from train_parse import train_path, test_path


def get_file(file_name):  # 获取数据集的文件名
    file_names = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        file_list = f.readlines()
    for i in file_list:
        file_names.append(i.strip('\n'))
    return file_names


def divide_file():  # 分割数据集
    file_names = get_file(file_path + 'train_val.txt')  # 获取到的数据集文件名列表
    train_size = int(0.8 * len(file_names))  # 训练集的大小
    test_size = len(file_names) - train_size  # 测试集的大小
    train_set, test_set = torch.utils.data.random_split(file_names, [train_size, test_size])  # 随机划分train:test = 8:2
    # 转换为列表
    train_set = list(train_set)
    test_set = list(test_set)
    # 保存文件
    # 训练集
    with open(file_path + 'train_set.txt', 'w', encoding='UTF-8') as f:
        for i in train_set:
            f.write(i + '\n')
    # 测试集
    with open(file_path + 'test_set.txt', 'w', encoding='UTF-8') as f:
        for i in test_set:
            f.write(i + '\n')


# 拷贝文件到新的文件夹中
def my_copy(old_path, new_path, file_name):
    shutil.copy(os.path.join(old_path, file_name), new_path)


def move_files():
    # file-类型字典
    file_kind = {}
    # 新的数据文件夹主目录
    new_path = './Data/train_val/'
    # 旧的数据集位置
    old_path = './garbage_classify/raw_data/'

    # 创建训练集位置
    if not os.path.exists(train_path):
        os.mkdir(train_path)
    # 创建测试集位置
    if not os.path.exists(test_path):
        os.mkdir(test_path)

    for i in range(40):
        # 创建各个数据集下的分类文件夹
        if not os.path.exists(train_path + str(i)):
            os.mkdir(train_path + str(i))
        if not os.path.exists(test_path + str(i)):
            os.mkdir(test_path + str(i))

    print('移动训练集...')
    train_set = get_file(file_path + 'train_set.txt')  # 读取训练集文件名
    for j in tqdm(range(len(train_set)), file=sys.stdout):  # 加上了进度显示
        i = train_set[j]  # 一个文件名
        s = get_file(old_path + i + '.txt')[0].split(', ')  # 分割出[文件名, 类型]
        file_kind[s[0]] = s[1]  # 记录下{文件名: 类型}
        my_copy(old_path, new_path + 'message', i + '.txt')  # 复制信息到message下
        my_copy(old_path, new_path + 'photo/train/' + s[1], i + '.jpg')  # 复制类型到train下的相应位置

    print('移动测试集...')
    test_set = get_file(file_path + 'test_set.txt')  # 读取测试集文件名
    # 同训练集处理
    for j in tqdm(range(len(test_set)), file=sys.stdout):
        i = test_set[j]
        s = get_file(old_path + i + '.txt')[0].split(', ')
        file_kind[s[0]] = s[1]
        my_copy(old_path, new_path + 'message', i + '.txt')
        my_copy(old_path, new_path + 'photo/test/' + s[1], i + '.jpg')
    with open('./Data/App_Data/file_kind.json', 'w', encoding='UTF-8') as f:
        json.dump(file_kind, f, indent=2, ensure_ascii=False)
    print('完成')


if __name__ == '__main__':
    # 分割数据集
    file_path = './Data/train_val/main/'  # 保存着数据集的文件名的地方
    divide_file()  # 分割数据集存至文件
    move_files()  # 根据上面分割保存的文件移动数据集
