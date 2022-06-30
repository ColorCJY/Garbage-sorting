# 综合课程设计Ⅲ
## 项目概述

基于机器视觉的垃圾分类

在ResNext101_32*16d_wsl的基础上进行的迁移学习（修改最后一层的全连接层）

进行了数据的统计、分割、简单预处理，读取采用datasets和DataLoader

训练完成后，在一个利用pyqt5开发的界面上进行预测展示

## 项目环境

```
目前的环境
windows 11 + GTX1650 4G
Anaconda -- python3.9 （自带安装了很多常用的库）
pytorch == 1.11.0 (若GPU：CUDA == 11.3)（推荐官网安装）
pyqt5 == 5.15.7
matplotlib == 3.5.1
hubconf.py https://github.com/facebookresearch/WSL-Images/blob/main/hubconf.py (Facebook开源框架)
```



## 项目结构

在windows操作系统下， xxx/Garbage-sorting

具体如下：

```
.../GARBAGE-SORTING  # 工程
│  deal_some_datas.py  # 处理分类规则成为自己的
│  divide_file.py  # 划分测试集/训练集
│  gui.ui  # Qt Designer 设计文件
│  hubconf.py  # 开源resnext101
│  main.py  # 主要界面
│  predict.py  # 预测图片
│  README.md  # 自述文件
│  read_file.py  # 统计数量并保存
│  run_train.py  # 分类训练测试器
│  statistics_photo.py  # 显示统计的数量并保存
│  train.py  # 驱动训练
│  train_parse.py  # 一些参数
│  UI_subjects.py  # 分割UI设计
│  utils.py  # 一些通用方法
├─Data  # 数据文件
│  ├─App_Data  # 程序产生的文件位置
│  │      other_files.json
│  │      
│  ├─img  # 程序运行的图片及产生的图片位置
│  │      box.png  # 界面上
│  │      logo.png  # 图标
│  │      
│  └─train_val  # 数据集
│      ├─main  # 三个txt文件名
│      ├─message  # 图片信息文件
│      ├─model  # 模型
│      └─photo  # 图片
│          ├─test  # 测试集
│          └─train  # 训练集
│
└─garbage_classify  # 源数据集位置
    │  garbage_classify_rule.json  # 原分类规则
    └─raw_data  # 图片及其信息位置
```

代码库里只有项目代码，数据集另需下载，暂未提供来源

## 项目运行

```
1.请按照以上项目结构中的存放格式进行文件的放置
2.注意安装所额外需要的库
3.运行顺序
（Tips：注意某些文件夹可能需要手动创建）
（1）deal_some_datas.py（Tip：形成自己的数据集分类规则）
（2）divide_file.py（Tip：分割数据集，使用分好的数据不用运行，之前的数据集可以删除）
（3）read_file.py （Tip：统计数量，显示数据集情况，并保存数据集情况）
（4）train.py （Tip：训练模型并保存）
（5）main.py（Tip：进行可视化展示预测结果）
注意：
采用未分割的数据集，可以自行更改或者注意创建一些文件夹
采用分割好的数据集可以直接第4步
若只是运行预测直接第5步
以上主要是一些文件位置会出现问题
```

