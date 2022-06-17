# 图示展示数据集中的情况 种类-数量
import matplotlib.pyplot as plt
import json

data_path = 'E:/Project/Python/Garbage/Data/test/data_num.json'  # 类型-num文件所在的文件夹
photo_path = 'E:/Project/Python/Garbage/Data/test/statistics_result.jpg'  # 保存统计结果


def get_data():
    # 获取数据
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def draw_plt():
    data = get_data()
    plt.figure(figsize=(16, 9), dpi=100)  # 图片的分辨率
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 图片的字体
    plt.ylabel('Num')  # y坐标名
    plt.xlabel('Type')  # x坐标名
    x = list(data.keys())  # x 类型
    y = list(data.values())  # y 数量
    r = plt.barh(x, y, height=0.5)  # 横着的坐标图
    # 标注数量在柱条右边
    for rect in r:
        wd = rect.get_width()
        plt.text(wd, rect.get_y() + 0.5 / 2, str(wd), va='center')
    plt.savefig(photo_path)  # 保存图片
    plt.show()  # 显示图片


if __name__ == '__main__':
    draw_plt()
