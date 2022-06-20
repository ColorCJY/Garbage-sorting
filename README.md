# 综合课程设计Ⅲ
## 项目概述

基于机器视觉的垃圾分类

## 项目环境

```
目前的环境
windows 11
Anaconda -- python3.9 （自带安装了很多常用的库）
pytorch == 1.11.0 (若GPU：CUDA == 11.3)
...待续
```



## 项目结构

在windows里文件管理为 E:/Project/Python/Garbage

具体如下：

```
Garbage
--Data  # 数据集及其他相关文件所在位置
----train_val  # 处理过的数据集
------main  # 三个txt文件，存储的一些文件名信息
--------train_val.txt  # 数据集文件名
--------train_set.txt  # 训练集文件名
--------test_set.txt  # 测试集文件名
------message  # 多个txt文件，存储图片以及图片中的相关信息
------photo  # 多个jpg文件，训练，测试的图片
------classify_rule.json  # 自己的分类规则
------...  # 其他程序产生数据文件
--Garbage-sorting  # 代码所在位置
----deal_some_datas  # 整理源数据集形成自己需要用的文件
----divide_file.py  # 划分数据集以及图形显示
----move_file.py  # 批量移动文件，一次移动一种文件
----read_file.py  # 读取文件信息形成其他的数据
----statistics_photo.py  # 统计各种垃圾类别的数量
----README.md  # 项目简单概况
--garbage_classify  # 源数据集【处理后可删除】
----raw_data  # 文件夹下有图片和图片的分类信息
----garba_classif_rule.json  # 源数据集的分类规则
...待续
```

代码库里只有项目代码，数据集另需下载，暂未提供来源

## 项目运行

```
1.请按照以上项目结构中的存放格式进行文件的放置（'-'的数量表示目录的级数）
2.注意安装所额外需要的库
3.运行顺序
（Tips：下面第一个文件可以跳过使用源数据集，但需要注意其他的更改）
deal_some_datas.py（Tip：形成自己的数据集，结束后可以手动删除源数据集了）
divide_file.py（Tip：总的显示训练集，分割训练集，图形化展示）
```

