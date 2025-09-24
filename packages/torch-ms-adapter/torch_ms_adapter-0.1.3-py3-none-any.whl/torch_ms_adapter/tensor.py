import mindspore.ops as ops

def flatten(x, start_dim=1):
    shape = x.shape
    new_shape = (shape[0], -1)
    return ops.Reshape()(x, new_shape)