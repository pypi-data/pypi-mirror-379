import mindspore.ops as ops

def relu(x):
    return ops.ReLU()(x)

def sigmoid(x):
    return ops.Sigmoid()(x)

def tanh(x):
    return ops.Tanh()(x)