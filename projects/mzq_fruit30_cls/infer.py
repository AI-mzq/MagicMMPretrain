# -*- coding:utf-8 -*-
# @Project:      MagicMMPretrain
# @Create Time : 2023/6/9 16:48
# @Author :      ai-mzq
# @File name:    infer.py
# @Software:     PyCharm

from mmpretrain import ImageClassificationInferencer

inference = ImageClassificationInferencer(
    'resnet50_fruit30.py', pretrained='exp/epoch_10.pth'
)

res = inference('2.jpg', show_dir='infer_result')
print(res)
