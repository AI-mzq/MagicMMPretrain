## MagicMMPretrain
- v1.0.0

### 简介：
- 基于OpenMMLab的mmpretrain库进行pretraining的实现。
- 实战项目结果文件路径为：projects/mzq_fruit30/

### 实战项目：基于 ResNet50 的水果分类
~~~
背景：使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类
任务 
1、划分训练集和验证集
2、按照 MMPreTrain CustomDataset 格式组织训练集和验证集
3、使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型
4、在水果数据集上进行微调训练
5、使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类
~~~

#### 训练命令：
~~~
mim train mmpretrain resnet50_fruit30.py --work-dir=./work_dir
~~~
#### 测试命令：
~~~
mim test mmpretrain resnet50_fruit30.py --checkpoint work_dir/epoch_10.pth
# 对测试结果进一步分析，生成结果文件
mim test mmpretrain resnet50_fruit30.py --checkpoint work_dir/epoch_10.pth --out result.pkl
~~~
#### 测试结果进一步评估分析命令
~~~
mim run mmpretrain analyze_results resnet50_fruit30.py result.pkl --out-dir analyze
~~~
#### 生成混淆矩阵命令
~~~
mim run mmpretrain confusion_matrix resnet50_fruit30.py result.pkl --include-values --show-path matrix_res.png
~~~