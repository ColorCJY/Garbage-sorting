# 根据pytorch的例子https://github.com/pytorch/examples/blob/master/imagenet/main.py
# 以及别人的实现进行的一些修改，将一些需要的函数或类进行抽取出来，适当修改减少在一个文件中的代码
import os
import torch
import torchvision.transforms as transforms

preprocess = transforms.Compose([
    transforms.Resize((256, 256)),  # 缩放最大边=256
    transforms.CenterCrop((224, 224)),
    transforms.ToTensor(),  # 归一化[0,1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
])


# 变量的更新AverageMeter类
class AverageMeter(object):
    """Computes and stores the average and current value
       Imported from https://github.com/pytorch/examples/blob/master/imagenet/main.py
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


# 计算准确率
def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"
          Imported from https://github.com/pytorch/examples/blob/master/imagenet/main.py
    """
    maxk = max(topk)
    batch_size = target.size(0)
    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))
    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


def save_checkpoint(state, is_best, checkpoint='checkpoint', filename='checkpoint.pth'):
    if not os.path.exists(checkpoint):
        os.makedirs(checkpoint)
    # 模型保存
    if is_best:
        model_name = 'best_' + filename
        model_path = os.path.join(checkpoint, model_name)
        torch.save(state, model_path)
        with open(os.path.join(checkpoint, 'state.txt'), 'w', encoding='UTF-8') as f:
            f.write(str(state['epoch']) + ', ' + str(state['best_acc']))
