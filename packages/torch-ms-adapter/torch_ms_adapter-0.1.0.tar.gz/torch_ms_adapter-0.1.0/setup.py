from setuptools import setup, find_packages

setup(
    name="torch-ms-adapter",
    version="0.1.0",
    description="PyTorch-style API adapter for MindSpore",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "mindspore",
        "numpy<2.0",
        "scikit-learn"
    ],
    python_requires=">=3.8",
)