# torch-ms-adapter

[![PyPI version](https://badge.fury.io/py/torch-ms-adapter.svg)](https://pypi.org/project/torch-ms-adapter/)
[![Python](https://img.shields.io/pypi/pyversions/torch-ms-adapter.svg)](https://pypi.org/project/torch-ms-adapter/)
[![License](https://img.shields.io/github/license/your-github-username/torch-ms-adapter.svg)](LICENSE)

torch-ms-adapter 是一个在 MindSpore 上模拟 PyTorch API 的适配器库。  
目标是让你几乎无需修改 PyTorch 代码，就能在 MindSpore 上运行。

## 特性
- 支持 nn.Module, Conv2d, Linear, ReLU, CrossEntropyLoss
- 封装了 DataLoader 和 Trainer（底层使用 MindSpore）
- 提供 torch.nn.functional 基本操作
- 自动屏蔽 PyTorch，兼容原始导入语句

## 安装
```bash
pip install torch-ms-adapter
```
## 使用示例
```
import torch_ms_adapter as torch
import torch_ms_adapter.nn as nn
import torch_ms_adapter.functional as F

class LeNet5(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.fc1 = nn.Linear(16*4*4, 120)
        self.fc2 = nn.Linear(120, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = torch.flatten(x, 1)
        x = self.fc2(F.relu(self.fc1(x)))
        return x
```
运行方式与pytorch一致，只需替换
```
import torch
```
为
```
import torch_ms_adapter as torch
```
## 路线图
- 支持基础层（linear,Conv2d,ReLU)
- 支持Loss函数
- 封装Optimizer
- 支持更多PyTorch模块（YOLO，ResNet）
- 完善Autograd

## 贡献
欢迎提交issue和PR，一起完善torch-ms-adopter