class SGD:
    def __init__(self, params, lr=0.01, momentum=0.0):
        self.params = list(params)
        self.lr = lr
        self.momentum = momentum
        self._grads = None

    def _set_grads(self, grads):
        self._grads = grads

    def step(self):
        for p, g in zip(self.params, self._grads):
            if g is not None:
                p.set_data(p - self.lr * g)

    def zero_grad(self):
        self._grads = None