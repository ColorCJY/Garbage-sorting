import torch.nn as nn
import torch.optim

from torchvision import datasets
from train_parse import *
from utils import save_checkpoint, preprocess
from torch.utils.data import DataLoader
from run_train import run_train


def train():
    # 加载数据
    pretrain.append('True')
    TRAIN = train_path
    VAL = test_path
    train_data = datasets.ImageFolder(root=TRAIN, transform=preprocess)
    val_data = datasets.ImageFolder(root=VAL, transform=preprocess)
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)
    print('数据加载完成，开始训练')
    # 初始化model
    model = run_train(num_classes)
    # 训练C类别的分类问题，用CrossEntropyLoss(交叉熵损失函数)
    criterion = nn.CrossEntropyLoss()
    # 优化器
    optimizer = torch.optim.Adam(model.model.parameters(), learning_rate)
    best_acc = 0
    for e in range(1, epoch + 1):
        print('[{}/{}] Training'.format(e, epoch))
        # train
        train_loss, train_acc = model.train_model(train_loader, criterion, optimizer)
        # evaluate
        test_loss, test_acc = model.evaluate(test_loader, criterion)
        # 用于判断是否保存模型
        is_best = test_acc > best_acc
        # 记录当前最好的acc
        best_acc = max(test_acc, best_acc)
        # 保存模型的文件名
        name = 'checkpoint' + '.pth'
        save_checkpoint({
            'epoch': e,
            'state_dict': model.model.state_dict(),
            'train_acc': train_acc,
            'test_acc': test_acc,
            'best_acc': best_acc,
            'optimizer': optimizer.state_dict()

        }, is_best, checkpoint=save_path, filename=name)
        print('Now acc:')
        print(test_acc)
        print('Best acc:')
        print(best_acc)


train()
