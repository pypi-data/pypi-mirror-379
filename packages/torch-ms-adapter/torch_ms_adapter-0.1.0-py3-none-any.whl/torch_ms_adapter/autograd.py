import mindspore.ops as ops


class TensorWithGrad:
    """包装 loss，使其拥有 backward() 方法"""
    def __init__(self, loss_value, model, loss_fn, inputs, targets, logits=None):
        self.value = loss_value
        self._model = model
        self._loss_fn = loss_fn
        self._inputs = inputs
        self._targets = targets
        self._logits = logits
        self._grads = None

    def backward(self, optimizer=None):
        """计算梯度并传给 optimizer"""

        def forward_fn(x, y):
            logits = self._model(x)
            # ✅ 注意取 .value，避免 TensorWithGrad 嵌套
            return self._loss_fn(logits, y).value

        grad_fn = ops.GradOperation(get_by_list=True)
        self._grads = grad_fn(forward_fn, self._model.trainable_params())(
            self._inputs, self._targets
        )

        if optimizer is not None:
            optimizer._set_grads(self._grads)
        return self._grads