# 通过训练好的模型预测图片的垃圾类别
import torch
import json
from PIL import Image
from run_train import run_train
from train_parse import num_classes
from utils import preprocess


# 读取标签对应的垃圾类别
def get_data(file):
    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)


# 标签采取的是字符串，torch处理时标签排序是字符串的排序，需要转换一下
def change_index():
    s = []
    for i in range(40):
        s.append(str(i))
    s.sort()
    dit = {}
    for i in range(len(s)):
        dit[i] = s[i]
    return dit


# 预测垃圾类别
class predict:
    def __init__(self):
        self.model_path = './Data/train_val/model/best_checkpoint.pth'  # 模型所在位置
        self.model = run_train(num_classes).model  # 用之前的训练模型（因为是迁移学习，所以需要进行更换成训练时的模型）
        self.model.load_state_dict(torch.load(self.model_path)['state_dict'])  # 加载模型的参数状态
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 选择进行计算的单元
        self.dit = change_index()  # 改变标签对应的顺序

    def predict_photo(self, img):
        self.model.eval()  # 预测需要选择eval模式
        with torch.no_grad():  # 不计算梯度
            image = Image.open(img)  # 打开图片
            img_change = preprocess(image).unsqueeze(0)  # 预处理及增加维数用于增加预测的标签
            img_change = img_change.to(self.device)  # 移到计算单元上
            outputs = self.model(img_change)  # 进行预测
        # 预测结果处理，通过softmax的处理将预测标签结果转化为概率
        outputs = torch.nn.functional.softmax(outputs[0], dim=0)
        # 上述的结果为张量，转化为列表，下标对应的为照片的类别0-39
        pred_list = outputs.cpu().numpy().tolist()
        # 取出最大值的下标
        index = pred_list.index(max(pred_list))
        # 取出下标对应的垃圾类型名
        name = get_data('./Data/App_Data/train_classes.json')[self.dit[index]]
        # 分类规则
        classify_rule = get_data('./Data/App_Data/classify_rule.json')
        # 得到垃圾类型名对应的是什么垃圾
        classify = ''
        for i in classify_rule:
            if name in classify_rule[i]:
                classify = i
        return classify, name
