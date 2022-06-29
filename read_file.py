# 统计数据集的每个类型的数量，并保存为json文件
import os

from statistics_photo import draw_plt, json


def save_json(file_name, dit):
    # 保存为json文件
    with open('./Data/App_Data/' + file_name, 'w', encoding='UTF-8') as f:
        json.dump(dit, f, indent=2, ensure_ascii=False)


def get_class_nums():
    data_path = './Data/train_val/photo/'  # 图片文件集位置
    with open('./Data/App_Data/train_classes.json', 'r', encoding='UTF-8') as f:
        train_classes = json.load(f)  # 读取序号：类型的json文件
    kinds_num = {}  # 总数据的类型：数量json文件
    train_num = {}  # 训练集的类型：数量json文件
    test_num = {}  # 测试集的类型：数量json文件
    for i in range(40):
        class_name = train_classes[str(i)]  # 当前的类型
        for root, file_dir, filename in os.walk(data_path + 'train/' + str(i)):  # 获取类型下的所有数据集文件名
            # 根据文件名的数量统计数量
            kinds_num[class_name] = len(filename)
            train_num[class_name] = len(filename)
        for root, file_dir, filename in os.walk(data_path + 'test/' + str(i)):  # 获取类型下的所有数据集文件名
            # 根据文件名的数量统计数量
            kinds_num[class_name] += len(filename)
            test_num[class_name] = len(filename)
    # 保存为文件
    save_json('kinds_num.json', kinds_num)
    save_json('train_num.json', train_num)
    save_json('test_num.json', test_num)


def view_train_val():
    # 图片显示，并保存
    draw_plt('./Data/img/train_val.jpg', './Data/App_Data/kinds_num.json', '数据集情况')
    draw_plt('./Data/img/train_num.jpg', './Data/App_Data/train_num.json', '训练集情况')
    draw_plt('./Data/img/test_num.jpg', './Data/App_Data/test_num.json', '测试集情况')


if __name__ == '__main__':
    get_class_nums()
    view_train_val()
