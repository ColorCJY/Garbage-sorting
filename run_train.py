# 模型的选择构建、训练、评估

import time

import numpy as np
import torch
import torch.nn as nn
from hubconf import *
from utils import AverageMeter, accuracy


class run_train:
    def __init__(self, num_classes, feature_extract=True):
        # 选择进行计算的单元（GPU|CPU）
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # 模型-设为全局变量 并且进行一定的修改
        self.model = self.setup_model(num_classes, feature_extract)

    # 模型的相关设置
    def setup_model(self, num_classes, feature_extract):
        # 选择resnext101_32x16d_wsl模型进行学习
        model = resnext101_32x16d_wsl()

        # 进行迁移学习，不需要反向修改所有的参数，先冻结模型的所有层参数，
        if feature_extract:
            for param in model.parameters():
                param.requires_grad = False

        # 然后再修改模型的最后一层输出层，进行训练输出层

        # 获取全连接层的输入特征
        in_feature = model.fc.in_features
        # 修改全连接层
        model.fc = nn.Sequential(
            nn.Dropout(0.2),  # 防止过拟合，表示每个神经元有x的可能性不被激活
            nn.Linear(in_features=in_feature, out_features=num_classes)
        )

        # 将model的训练放到选择的训练单元
        model.to(self.device)
        return model

    # 训练模型
    def train_model(self, train_loader, criterion, optimizer):
        # 定义几个需要更新的变量
        data_time = AverageMeter()
        batch_time = AverageMeter()
        losses = AverageMeter()
        top1 = AverageMeter()
        end = time.time()

        # 选择train mode
        self.model.train()

        # batch的序号，（输入的图片，分类）
        for batch_index, (images, labels) in enumerate(train_loader):
            # 记录时间 measure data loading time
            data_time.update(time.time() - end)
            # 将输入的数据，标识送到选择的单元
            images, labels = images.to(self.device), labels.to(self.device)

            # 计算输出,先进行zero_grad清空梯度的累积
            optimizer.zero_grad()
            # 计算模型，得出loss
            output = self.model(images)
            loss = criterion(output, labels)
            # 反向传播
            loss.backward()
            # 更新权重参数
            optimizer.step()

            # 计算ACC和变量更新
            acc1, _ = accuracy(output.data, labels.data, topk=(1, 1))
            losses.update(loss.item(), images.size(0))
            top1.update(acc1.item(), images.size(0))
            batch_time.update(time.time() - end)
            end = time.time()

            print('({batch}/{size}) | Loss: {loss:.4f} | top1: {top1: .4f}'.format(batch=batch_index + 1,
                                                                                   size=len(train_loader),
                                                                                   loss=losses.avg,
                                                                                   top1=top1.avg
                                                                                   ))
        return losses.avg, top1.avg

    # 模型评估
    def evaluate(self, test_loader, criterion, test=None):

        batch_time = AverageMeter()
        data_time = AverageMeter()
        losses = AverageMeter()
        top1 = AverageMeter()
        end = time.time()

        predict_all = np.array([], dtype=int)  # 预测
        labels_all = np.array([], dtype=int)  # 真实

        # 进行评估时需要选择 the eval model
        self.model.eval()

        # 预测每批数据，进行模型的评估
        for batch_index, (images, labels) in enumerate(test_loader):
            data_time.update(time.time() - end)
            # move tensors to GPU if cuda is_available
            images, labels = images.to(self.device), labels.to(self.device)
            # 模型的预测
            outputs = self.model(images)
            # 计算loss
            loss = criterion(outputs, labels)

            # 计算acc和变量更新
            acc1, _ = accuracy(outputs.data, labels.data, topk=(1, 1))
            losses.update(loss.item(), images.size(0))
            top1.update(acc1.item(), images.size(0))
            batch_time.update(time.time() - end)
            end = time.time()

            # 评估混淆矩阵的数据
            labels = labels.data.cpu().numpy()  # 真实数据的y数值
            predict = torch.max(outputs.data, 1)[1].cpu().numpy()  # 预测数据y数值
            labels_all = np.append(labels_all, labels)  # 数据赋值
            predict_all = np.append(predict_all, predict)

            print('({batch}/{size}) | Loss: {loss:.4f} | top1: {top1: .4f}'.format(batch=batch_index + 1,
                                                                                   size=len(test_loader),
                                                                                   loss=losses.avg,
                                                                                   top1=top1.avg
                                                                                   ))

        if test:
            return losses.avg, top1.avg, predict_all, labels_all
        else:
            return losses.avg, top1.avg
