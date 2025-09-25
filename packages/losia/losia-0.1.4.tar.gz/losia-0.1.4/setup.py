# setup.py
from setuptools import setup, find_packages

setup(
    name="losia",
    version="0.1.4",
    author="Xujia Wang",
    author_email="wang-xj22@mails.tsinghua.edu.cn",
    description="An resource-efficient fine-tuning toolkit that tunes model via subnet-structured optimization, localization, and integration.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KlozeWang/LoSiA",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.8",
    license="Apache-2.0",
    install_requires=[
        "bitsandbytes",
        "datasets",
        "loguru",
        "matplotlib",
        "numpy",
        "tensorly",
        "torch",
        "tqdm",
        "transformers",
        "ninja",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)