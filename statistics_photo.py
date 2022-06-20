# 图示展示数据集中的情况 种类-数量
import matplotlib.pyplot as plt
import json


def get_data(data_path):
    # 获取数据
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def draw_plt(photo_path, data_path, title):
    data = get_data(data_path)  # 读取数据
    plt.figure(figsize=(16, 9), dpi=100)  # 图片的分辨率
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 图片的字体
    plt.ylabel('Type')  # y坐标名
    plt.xlabel('Num')  # x坐标名
    plt.title(title)  # 图表标题
    x = list(data.keys())  # x 类型
    y = list(data.values())  # y 数量
    r = plt.barh(x, y, height=0.5)  # 横着的坐标图
    # 标注数量在柱条右边
    for rect in r:
        wd = rect.get_width()
        plt.text(wd, rect.get_y() + 0.5 / 2, str(wd), va='center')
    plt.savefig(photo_path)  # 保存图片
    plt.show()  # 显示图片
