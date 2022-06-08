# 图示展示数据集中的情况 种类-数量
import matplotlib.pyplot as plt
import json

data_path = '../Data/test/data_num.json'


def get_data():
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def draw_plt():
    data = get_data()
    plt.figure(figsize=(16, 9), dpi=80)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.ylabel('Type')
    plt.xlabel('Num')
    x = list(data.keys())
    y = list(data.values())
    r = plt.barh(x, y, height=0.5)
    for rect in r:
        wd = rect.get_width()
        plt.text(wd, rect.get_y() + 0.5 / 2, str(wd), va='center')
    plt.show()


if __name__ == '__main__':
    draw_plt()
