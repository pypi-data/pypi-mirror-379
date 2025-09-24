import sys

# ================== 屏蔽真实 PyTorch ==================
if 'torch' in sys.modules:
    del sys.modules['torch']

# ================== NumPy 自动降级 ==================
try:
    import numpy as np
    ver = tuple(map(int, np.__version__.split('.')[:2]))
    if ver >= (2, 0):
        print(f"[WARN] 检测到 NumPy {np.__version__} 与 MindSpore 不兼容，正在降级到 1.26.4 ...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==1.26.4"])
        import importlib
        importlib.reload(np)
except Exception as e:
    print("[WARN] NumPy 版本检测失败：", e)

# ================== 导入 adapter 子模块 ==================
from . import nn
from .nn import functional   # 👈 注意 functional 在 nn 里面
from . import optim
from . import tensor
from . import data
from . import training

# ================== 注册成 torch ==================
sys.modules['torch'] = sys.modules[__name__]
sys.modules['torch.nn'] = nn
sys.modules['torch.nn.functional'] = functional
sys.modules['torch.optim'] = optim
sys.modules['torch.utils'] = {}
sys.modules['torch.utils.data'] = data
sys.modules['torch.tensor'] = tensor
sys.modules['torch.training'] = training

# 常用函数直接挂载
flatten = tensor.flatten