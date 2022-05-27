import torch
from torchvision import datasets, transforms

batch_size = 200

"""读取训练集和测试集"""
train_db = datasets.MNIST('../data', train=True, download=True,
                          transform=transforms.Compose([
                              transforms.ToTensor(),
                              transforms.Normalize((0.1307,), (0.3081,))
                          ]))

"""刚读取进来的"""
print('train:', len(train_db))

"""将训练集划分为训练集和验证集"""
train_db, val_db = torch.utils.data.random_split(train_db, [50000, 10000])
print('train:', len(train_db), 'validation:', len(val_db))

"""
这一步是将torch.utils.data.dataset.Subset
转换成torch.utils.data.dataloader.DataLoader
根据batch_size让它多出了一个"批编号"的维度
"""
# 训练集
train_loader = torch.utils.data.DataLoader(
    train_db,
    batch_size=batch_size, shuffle=True)
# 验证集
val_loader = torch.utils.data.DataLoader(
    val_db,
    batch_size=batch_size, shuffle=True)
