import os
import numpy as np
import mindspore
from mindspore.dataset import GeneratorDataset, transforms

# ==================== MNIST 数据准备 ====================
def _prepare_mnist_npy(dataset_dir="./MNIST_Data"):
    """如果没有 .npy 文件则从 OpenML 下载并保存"""
    need_download = False
    train_images = os.path.join(dataset_dir, 'train', 'images.npy')
    train_labels = os.path.join(dataset_dir, 'train', 'labels.npy')
    test_images  = os.path.join(dataset_dir, 'test',  'images.npy')
    test_labels  = os.path.join(dataset_dir, 'test',  'labels.npy')

    if not os.path.exists(dataset_dir):
        need_download = True
    else:
        for p in [train_images, train_labels, test_images, test_labels]:
            if not os.path.exists(p):
                need_download = True
                break

    if not need_download:
        return

    os.makedirs(os.path.join(dataset_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(dataset_dir, 'test'),  exist_ok=True)

    print("[INFO] 正在从 OpenML 下载 MNIST（仅首次，需要网络）...")
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist.data, mnist.target.astype(np.int32)

    X = X.reshape(-1, 28, 28)
    y = y.astype(np.int32)

    X_train, y_train = X[:60000], y[:60000]
    X_test,  y_test  = X[60000:], y[60000:]

    np.save(train_images, X_train)
    np.save(train_labels, y_train)
    np.save(test_images,  X_test)
    np.save(test_labels,  y_test)
    print(f"[INFO] MNIST 保存到 {dataset_dir}")

# ==================== 数据集构造 ====================
def create_dataset(batch_size=64, is_train=True, dataset_dir="./MNIST_Data", shuffle_size=1000):
    _prepare_mnist_npy(dataset_dir)

    split = 'train' if is_train else 'test'
    images = np.load(os.path.join(dataset_dir, split, 'images.npy'))
    labels = np.load(os.path.join(dataset_dir, split, 'labels.npy')).astype(np.int32)

    # 👇 强制 reshape，保证是一维 (N,)
    labels = labels.reshape(-1)

    def generator():
        for img, lab in zip(images, labels):
            img = (img.astype(np.float32) / 255.0)[None, :, :]  # (1,28,28)
            yield img, int(lab)  # 👈 确保 label 是 Python int

    ds = GeneratorDataset(source=generator, column_names=['image', 'label'], shuffle=is_train)

    ds = ds.map(operations=transforms.TypeCast(mindspore.int32), input_columns='label')

    if is_train:
        ds = ds.shuffle(buffer_size=shuffle_size)
    ds = ds.batch(batch_size, drop_remainder=True)
    return ds
# ==================== PyTorch 风格 DataLoader ====================
class DataLoader:
    def __init__(self, dataset_dir="./MNIST_Data", batch_size=64, train=True):
        self.ds = create_dataset(batch_size=batch_size, is_train=train, dataset_dir=dataset_dir)

    def __iter__(self):
        for img, lab in self.ds.create_tuple_iterator():
            yield img, lab.squeeze()   # 👈 确保 batch 标签是一维 (batch,)