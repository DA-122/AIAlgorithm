import torch
import math
import torch.utils.data as data
from torchvision import transforms
from PIL import Image
import os
import matplotlib.pyplot as plt


# 数据集类，需要给data basedir、imgs路径和labels列表
class MyImageDataset(data.Dataset):
    def __init__(self,base_dir,imgs,labels,transform,mode = 'train'):
        super(MyImageDataset,self).__init__()
        datas = []
        for img, label in zip(imgs,labels):
            datas.append((img,label))
        self.datas = datas
        self.base_dir = base_dir
        self.mode = mode
        if self.mode == 'train':
            self.trans = transform
        else:
            self.trans = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor()
            ])

    def __len__(self):
        return len(self.datas)
    
    def __getitem__(self, index):
        img,label = self.datas[index]
        img = self.trans(Image.open(os.path.join(self.base_dir,img)))
        return img,label
    

def show_imgs(num_cols,dirs=None,imgs =None,titles = None,scale = 3):
    if dirs:
        imgs = [Image.open(dir) for dir in dirs]
    num = len(imgs)
    num_rows = int(math.ceil(num / num_cols))
    plt.figure(num_rows*num_cols*scale)
    axes = []
    for i in range(len(imgs)):
        axe = plt.subplot(num_rows, num_cols,i+1)
        axes.append(axe)

    for i, (axe,img) in enumerate(zip(axes,imgs)):
        if torch.is_tensor(img):
            axe.imshow(img.permute(1,2,0).numpy())
        else:
            axe.imshow(img)
        axe.axes.get_xaxis().set_visible(False)
        axe.axes.get_yaxis().set_visible(False)
        if titles:
            axe.set_title(titles[i])

