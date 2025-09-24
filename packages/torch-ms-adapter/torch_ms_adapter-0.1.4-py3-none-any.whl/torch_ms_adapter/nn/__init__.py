import mindspore.nn as msnn
import mindspore as ms
import numpy as np
from ..autograd import TensorWithGrad


class Module(msnn.Cell):
    def __init__(self):
        super(Module, self).__init__()

    def forward(self, *inputs, **kwargs):
        raise NotImplementedError

    def construct(self, *inputs, **kwargs):
        return self.forward(*inputs, **kwargs)

    def parameters(self):
        return self.trainable_params()


class Conv2d(msnn.Conv2d):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, bias=True):
        pad_mode = 'pad' if padding > 0 else 'valid'
        super().__init__(in_channels, out_channels, kernel_size,
                         stride=stride, pad_mode=pad_mode, has_bias=bias)


class Linear(msnn.Dense):
    def __init__(self, in_features, out_features, bias=True):
        super().__init__(in_features, out_features, has_bias=bias)


class MaxPool2d(msnn.MaxPool2d):
    def __init__(self, kernel_size, stride=None):
        stride = stride or kernel_size
        super().__init__(kernel_size=kernel_size, stride=stride)


class AvgPool2d(msnn.AvgPool2d):
    def __init__(self, kernel_size, stride=None):
        stride = stride or kernel_size
        super().__init__(kernel_size=kernel_size, stride=stride)


class ReLU(msnn.ReLU):
    def __init__(self):
        super().__init__()


class CrossEntropyLoss(msnn.SoftmaxCrossEntropyWithLogits):
    """
    PyTorch 风格的 CrossEntropyLoss 适配到 MindSpore。
    自动保证 labels 为 1D (N,)。
    """
    def __init__(self):
        super().__init__(sparse=True, reduction="mean")
        self._model = None
        self._inputs = None

    def bind(self, model, inputs):
        """绑定当前 batch 的 model 和 inputs，供 backward 使用"""
        self._model = model
        self._inputs = inputs

    def __call__(self, logits, targets):
        # 确保 targets 一维
        if hasattr(targets, "asnumpy"):  # MindSpore Tensor
            t = targets.asnumpy()
            targets = ms.Tensor(t.reshape(-1), dtype=ms.int32)
        elif isinstance(targets, np.ndarray):
            targets = ms.Tensor(targets.reshape(-1).astype(np.int32))
        else:
            targets = ms.Tensor(np.array(targets).reshape(-1).astype(np.int32))

        loss_value = super().__call__(logits, targets)

        # ✅ 返回 TensorWithGrad
        return TensorWithGrad(loss_value, self._model, self, self._inputs, targets, logits)