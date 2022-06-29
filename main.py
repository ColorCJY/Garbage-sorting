import ctypes
import sys  # 必要部分1：必须导入sys模块
import time
import os

from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog  # 必要部分2：QMainWindow可以提供.show()方法，从而展示窗口
from UI_subjects import *  # 必要部分3：计算两个数字.py是生成界面的文件
from predict import predict


class window(QMainWindow, Ui_MainWindow):  # 必要部分4：将页面文件汇集过来
    def __init__(self):
        super(window, self).__init__()  # 必要部分5：用类window（）继承
        self.animation = None
        self.history = './'  # 历史选择路径
        self.classify_name = ''  # 对应四种分类的类型名
        print('系统初始化中...')
        s = time.time()
        self.pre = predict()  # 预测对象
        self.setupUi(self)  # 必要部分6：
        self.imgNamepath = ''  # 默认图片文件的位置为空
        self.pushButton.clicked.connect(self.openImage)
        self.pushButton_2.clicked.connect(self.identification)
        self.pushButton_3.clicked.connect(self.classify)
        self.img = QtGui.QPixmap("./Data/img/box.png").scaled(self.label.width(), self.label.height())
        # 在label控件上显示选择的图片
        self.label.setPixmap(self.img)
        print('系统初始化完成，用时{:.1f}s'.format(time.time()-s))

    def animationFinished(self):
        time.sleep(1)
        self.moveImage2(318, 400, 10)
        self.label_2.setPixmap(QPixmap(""))

    # 选择本地图片上传
    def openImage(self):
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        self.label_3.setText('')  # 重新打开文件清空预测的分类
        self.imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget, "选择图片",
                                                                self.history, "*.jpg;;*.jpeg;;*.png")
        if self.imgNamepath:
            self.history = os.path.split(self.imgNamepath)[0]
            print(self.imgNamepath)
            # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
            img = QtGui.QPixmap(self.imgNamepath).scaled(self.label_2.width(), self.label_2.height())
            # 在label控件上显示选择的图片
            self.label_2.setPixmap(img)
        else:
            self.label_2.clear()  # 没有选择，清空界面显示（本来没有无影响）

    def identification(self):
        if self.imgNamepath:  # 需要选择了图片才会有
            self.classify_name, name = self.pre.predict_photo(self.imgNamepath)
            self.label_3.setText(name)
        else:
            self.label_3.setText('')  # 否则为清空

    def classify(self):
        if self.imgNamepath and self.label_3.text():  # 需要选择了照片并进行了预测
            img = QtGui.QPixmap(self.imgNamepath).scaled(50, 50)
            self.label_2.setPixmap(img)
            if self.classify_name == '有害垃圾':
                self.moveImage(318, 430, 2000)

    def moveImage(self, x, y, t):
        self.animation = QPropertyAnimation(self.label_2, b'pos')
        self.animation.setDuration(t)
        self.animation.setStartValue(QPoint(19, 19))
        self.animation.setEndValue(QPoint(x, y))
        self.animation.setLoopCount(1)
        self.animation.finished.connect(self.animationFinished)
        self.animation.start()

    def moveImage2(self, x, y, t):
        self.animation = QPropertyAnimation(self.label_2, b'pos')
        self.animation.setDuration(t)
        self.animation.setStartValue(QPoint(x, y))
        self.animation.setEndValue(QPoint(19, 19))
        self.animation.setLoopCount(1)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    main = window()
    main.setWindowIcon(QIcon('./Data/img/logo.png'))
    main.setWindowTitle("垃圾分类")
    main.show()
    sys.exit(app.exec_())
