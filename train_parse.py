# 训练模型所用的一些参数

"""固定位置参数"""
data_path = './Data/'  # 数据所在位置

photo_path = data_path + 'train_val/photo/'  # 照片所在位置

train_path = data_path + 'train_val/photo/train/'  # 训练集位置

test_path = data_path + 'train_val/photo/test/'  # 测试集位置

save_path = data_path + 'train_val/model/'  # 训练好模型保存的地方

""""以下调整训练中的超参数"""
# 学习率 决定着目标函数能否收敛到局部最小值以及何时收敛到最小值
learning_rate = 0.001  # 默认0.001，如结果不怎么好，进行更改
# 分批数据的大小
batch_size = 16  # 设置合理，需要根据收敛情况以及显存等的情况来定
# 遍历所有数据的次数
epoch = 10  # 适当调整
# 训练出来的分类数量
num_classes = 40  # 40种垃圾
