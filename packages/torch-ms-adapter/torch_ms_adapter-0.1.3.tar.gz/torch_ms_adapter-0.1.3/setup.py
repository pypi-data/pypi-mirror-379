from setuptools import setup, find_packages

# 读取 README.md 作为长描述
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="torch-ms-adapter",  # PyPI 上的包名
    version="0.1.3",  # ⚠️ 每次上传必须改新版本号
    author="danny",
    author_email="daizelin@icloud.com",
    description="A PyTorch adapter running on MindSpore",
    long_description=long_description,  # 用 README.md 作为描述
    long_description_content_type="text/markdown",  # 告诉 PyPI 用 Markdown 渲染
    url="https://github.com/your-username/torch-ms-adapter",  # 可选：GitHub 地址
    packages=find_packages(),
    install_requires=[
        "mindspore",
        "numpy<2.0",
    ],
    python_requires=">=3.7",
    classifiers=[  # 分类器，可选
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)