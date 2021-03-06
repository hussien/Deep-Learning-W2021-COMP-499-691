# -*- coding: utf-8 -*-
"""Final_EfficientNetB0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ro9TuMNAPnR9SG4wXsJdd6uI9-8TeoGU
"""

import os.path
from os import path
if path.exists("/content/cifar10_pytorch") == False:
  !git clone https://github.com/hussien/cifar10_pytorch.git

!pip install wget

# if path.exists("/content/CINIC-10.zip") == False:
#   !wget -O 'CINIC-10.zip' 'https://storage.googleapis.com/kaggle-data-sets/362150/707954/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210430%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210430T012007Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=5190655eddffb25894ecfde1e51a8ba51556c3cc0e7d4fe1852cf3a2ac9a79261396a8c820160e2018c75e1a9a8a0f71c9425613db48f9175da09e77cd3f21a758d3a9800ce75a40888f701cdd00282ca77b916301c054cbb831780ec56d6133c16bc14f6419b07c4d94af6c23acc911a1dcbe7116ea61d5d49a38a6c49bd2f96898daa1aacc3e928a77015ad671ffd54ccf17eae7e8aeea6686e90c3fd5d0b5729e8e6b0554980b13dd56728c3395664b0eb94897ea5de563c96940407de868d810c865d021a4a544785719308fa220ceaedb799e8ceef66f5ebc39c719319f48f94d8fa0d098515ca9d0182f76a1a22f2aa432c19046a3db38823f963ccdc6'

# if path.exists("/content/CINIC-10") == False:
#   !unzip -q  '/content/CINIC-10.zip' -d '/content/CINIC-10'

# from google.colab import drive
# drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
import torch
from torchvision import datasets, models, transforms
import torch.nn as nn
from torch.nn import functional as F
import torch.optim as optim

import os
import torch
import torchvision
import tarfile
import numpy as np
import torch.nn.functional as F
from torchvision.datasets.utils import download_url
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import torchvision.transforms as tt
from torch.utils.data import random_split
from torchvision.utils import make_grid
import matplotlib
import matplotlib.pyplot as plt

!pip install yacs

import os
import argparse
import torch
import os, sys
from cifar10_pytorch.cifar10_pytorch.engine import train, test
from cifar10_pytorch.cifar10_pytorch.config import cfg
from cifar10_pytorch.cifar10_pytorch.modeling import build_model

# ! rm -r 'CINIC-10-Filtered_1K'

if path.exists("/content/CINIC-10-Filtered_1K") == False:
  !unzip -q  '/content/cifar10_pytorch/CINIC-10-Filtered_1K.zip' -d '/content/'
if path.exists("train") == False:
  !unzip -q  '/content/cifar10_pytorch/train.zip' -d '/content/'
if path.exists("/content/test") == False:
  !unzip -q  '/content/cifar10_pytorch/test.zip' -d '/content/'

def arg_parser():
    parser = argparse.ArgumentParser(description="CIFAR10 training")
    parser.add_argument(
        "--config",
        # default='/content/cifar10_pytorch/configs/efficientnetB0.yaml',
        default='/content/cifar10_pytorch/configs/efficientnetB1.yaml',
        help="path to config file",
        type=str
    )
    parser.add_argument(
        '--tfboard', help='tensorboard path for logging', type=str, default='out')
    parser.add_argument('--checkpoint_dir', type=str,
                        default='checkpoints',
                        help='directory where checkpoint files are saved')
    parser.add_argument('--resume', type=str,
                        default=None,
                        help='checkpoint file path')
    return parser.parse_args("")

!pip install tensorboardX

# args and configs
args = arg_parser()
if args.config:
    cfg.merge_from_file(args.config)
cfg.freeze()
os.makedirs(args.checkpoint_dir, exist_ok=True)

# Model definition
# cfg.SOLVER.BATCHSIZE=64
model = build_model(cfg)
# cfg.MODEL.DEVICE='cpu'
print(cfg.MODEL.DEVICE)
device = cfg.MODEL.DEVICE
model.to(device)

# Optimizer settings
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),
                            lr=cfg.SOLVER.BASE_LR,
                            momentum=cfg.SOLVER.MOMENTUM,
                            weight_decay=cfg.SOLVER.WEIGHT_DECAY,
                            )

scheduler = torch.optim.lr_scheduler.MultiStepLR(
    optimizer,
    cfg.SOLVER.MILESTONES,
    cfg.SOLVER.GAMMA,
)

import torch
import torchvision
from torchvision import datasets,transforms
import torchvision.transforms as T

def build_transforms(cfg, is_train=True):
    list_transforms = list()
    print("cfg.DATA.IMG_SIZE=",cfg.DATA.IMG_SIZE)
    # Resizing. Some models must have ImageNet-size images as input
    if is_train and cfg.DATA.IMG_SIZE != 32:
        list_transforms.append(T.Resize((cfg.DATA.IMG_SIZE, cfg.DATA.IMG_SIZE)))
    elif is_train == False and cfg.TEST.IMG_SIZE != 32:
        list_transforms.append(T.Resize((cfg.DATA.IMG_SIZE, cfg.DATA.IMG_SIZE)))

    if is_train:
        if cfg.DATA.RANDOMCROP:
            list_transforms.append(T.RandomCrop(cfg.DATA.IMG_SIZE, padding=4))
        if cfg.DATA.LRFLIP:
            list_transforms.append(T.RandomHorizontalFlip())

    list_transforms.extend([
        T.ToTensor(),
        T.Normalize(cfg.DATA.NORMALIZE_MEAN, cfg.DATA.NORMALIZE_STD),
    ])

    transforms = T.Compose(list_transforms)

    return transforms

from numpy.random import RandomState
from torch.utils.data import Subset

def prepare_cifar10_dataset(cfg):
    """ prepare CIFAR10 dataset based on configuration"""

    transform_train = build_transforms(cfg, is_train=True)
    transform_test = build_transforms(cfg, is_train=False)


    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

    # dataset_train = torchvision.datasets.CIFAR10(
    #     root='./data',
    #     train=True,
    #     download=True,
    #     transform=transform_train
    # )
    dataset_train = datasets.ImageFolder(
            '/content/CINIC-10-Filtered_1K/train',
            transform=transform_train
    )
    dataloader_train = torch.utils.data.DataLoader(
        dataset_train,
        batch_size=cfg.SOLVER.BATCHSIZE,
        shuffle=True,
        num_workers=cfg.SOLVER.NUM_WORKERS
    )
    dataset_valid = torchvision.datasets.CIFAR10(
        root='./data',
        train=False,
        download=True,
        transform=transform_test
    )
  
    prng = RandomState(10)
    random_permute = prng.permutation(np.arange(0, 1000))
    print(len(dataset_valid.targets))
    indx_val = np.concatenate([np.where(np.array(dataset_valid.targets) == classe)[0][random_permute[10:210]] for classe in range(0, 10)])
    val_data = Subset(dataset_valid, indx_val)

    print('Num Samples For Val= %d'%(val_data.indices.shape[0]))

    dataloader_valid = torch.utils.data.DataLoader(
        val_data,
        batch_size=cfg.TEST.BATCHSIZE,
        shuffle=False,
        num_workers=cfg.SOLVER.NUM_WORKERS
    )

    return dataloader_train, dataloader_valid

dataloader_train, dataloader_test = prepare_cifar10_dataset(cfg)
# print(len(dataloader_train.dataset))

"""training settings:

Model:
  PRETRAINED: "EfficientNetB0"
  DROPOUT_RATE: 0.2

Augmentation:
  IMG_SIZE: 224
  RANDOMCROP: True

SOLVER:
  LR: 0.015
  BATCHSIZE: 64
  END_EPOCH : 30
  WEIGHT_DECAY: 0.0001

"""

# if args.resume:
#     checkpoint = torch.load(args.resume)
#     model.load_state_dict(checkpoint['model_state_dict'])
#     optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
#     scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
#     #scheduler.last_epoch = checkpoint['epoch']
#     start_epoch = checkpoint['epoch']
# else:
#     start_epoch = 0

end_epoch = 30
train_loss_epoch,valid_loss_epoch=[],[]
train_acc_epoch,valid_acc_epoch=[],[]
for epoch in range(0, end_epoch):
    scheduler.step()
    print("------ start epoch {} / {} with lr = {:.5f} -----".format(
        epoch+1, end_epoch, scheduler.get_lr()[0])
    )
    train_loss, train_acc = train(model, device, dataloader_train, criterion, optimizer, epoch)
    train_loss_epoch.append(train_loss)
    train_acc_epoch.append(train_acc)
    # if epoch%5 == 0:
    valid_loss, valid_acc = test(model, device, dataloader_test, criterion, epoch)
    valid_loss_epoch.append(valid_loss)
    valid_acc_epoch.append(valid_acc)

"""#### Save Traind Model """

import datetime 
currentDT = datetime.datetime.now()
torch.save({'epoch': epoch + 1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'scheduler_state_dict': scheduler.state_dict(),
            'train_loss_epoch': train_loss_epoch,
            'test_loss_epoch': valid_loss_epoch,
            'train_acc_epoch': train_acc_epoch,
            'test_acc_epoch': valid_acc_epoch
            },
            os.path.join("/content/", "EfficientNetB0_CINIC10_30epoch_"+str(currentDT)+".ckpt"))

"""#### Load Trained Model"""

checkpoint = torch.load('/content/cifar10_pytorch/ModelPickles/EfficientNetB0_CINIC10_30epoch_20210430_R3.ckpt')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
train_loss_epoch = checkpoint['train_loss_epoch']
valid_loss_epoch=checkpoint['test_loss_epoch']
train_acc_epoch=checkpoint['train_acc_epoch']
valid_acc_epoch=checkpoint['test_acc_epoch']

accs = np.array(valid_acc_epoch)
print('Acc over 2 instances: %.2f +- %.2f'%(accs.mean(),accs.std()))

"""#### Model Evaluation with CIFAR10 test set"""

model.eval()
test_loss = 0
correct = 0
total = 0
with torch.no_grad():
        for batch_i, (inputs, targets) in enumerate(dataloader_test):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()
            if batch_i > 0 and (batch_i + 1) % 100 == 0:
                print("test-> epoch {}, iter {} / {}, Loss: {:.3f} | Acc: {:.3f}".format(
                    epoch+1,
                    batch_i+1,
                    len(dataloader_test),
                    test_loss/(batch_i+1),
                    100.*correct/total,
                ))
acc = 100.*correct/total
print("Accuracy: {:.4f}".format(acc))

# loss_train = history.history['train_loss']
# loss_val = history.history['val_loss']
loss_train=train_loss_epoch
loss_test=valid_loss_epoch
epochs = range(1,len(train_loss_epoch)+1)
plt.plot(epochs, loss_train, label='CINIC Train loss')
plt.plot(epochs, loss_test, label='MNIST Test loss')
plt.title('EfficentNet-B0 Training and Test loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

epochs = range(1,len(valid_acc_epoch)+1)
plt.plot(epochs, train_acc_epoch, label='CINIC Train Acc')
plt.plot(epochs, valid_acc_epoch, label='MNIST Test Acc')
plt.title('EfficentNet-B0 Training and test Acc')
plt.xlabel('Epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()

# !unzip -q  '/content/gdrive/MyDrive/DLCourseProject/train.zip' -d '/content/train'
# !unzip -q  '/content/gdrive/MyDrive/DL_Course/test.zip' -d '/content/test'

from cifar10_pytorch.cifar10_pytorch.data import transform
validation_img_paths = []
transform_test = transform.build_transforms(cfg, is_train=False)
for i in range(1,51):
  validation_img_paths.append("/content/test/all/"+str(i).zfill(4)+".png")
img_list = [Image.open( img_path) for img_path in validation_img_paths]

validation_batch = torch.stack([transform_test(img).to(device)
                                for img in img_list])

pred_logits_tensor = model(validation_batch)
pred_probs = F.softmax(pred_logits_tensor, dim=1).cpu().data.numpy()
classes=['airplane','automobile','bird', 'cat','deer', 'dog', 'frog','horse', 'ship',  'truck']
fig, axs = plt.subplots(10, 5, figsize=(10, 20))
for i, img in enumerate(img_list):
    ax = axs[int(i/5),i%5]
    ax.axis('off')
    # print(pred_probs[i])
    ax.set_title(str(np.argmax(pred_probs[i]))+" "+classes[np.argmax(pred_probs[i])])                                                        
    ax.imshow(img)

