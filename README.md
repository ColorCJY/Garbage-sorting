# 综合课程设计Ⅲ
## 项目概述

基于机器视觉的垃圾分类

## 项目环境

```
目前的环境
windows 11
Anaconda -- python3.9
pytorch == 1.11.0 (若GPU：CUDA == 11.3)
...待续
```



## 项目结构

在windows里文件管理为 E:/Project/Python/Garbage

具体如下：

```
Garbage
--Data  # 数据集所在位置
----test  # 初步编码进行测试使用的数据集（少量）
------main  # 三个txt文件，存储的一些文件名信息
--------train_val.txt  # 数据集文件名
--------train_set.txt  # 训练集文件名
--------test_set.txt  # 测试集文件名
------message  # 多个xml文件，存储图片以及图片中的信息
------photo  # 多个jpg文件，训练，测试的图片
------classify_rule.json  # 分类规则
------...  # 其他程序产生数据文件
----train_val  # 与test相同，数据集较多
--Garbage-sorting  # 代码所在位置
----divide_file.py  # 划分数据集
----move_file.py  # 批量移动文件，一次移动一种文件
----read_file.py  # 读取文件信息
----statistics_photo.py  # 统计各种垃圾类别的数量
----README.md  # 项目简单概况
...待续
```

代码库里只有项目代码，数据集另需下载，暂未提供来源
