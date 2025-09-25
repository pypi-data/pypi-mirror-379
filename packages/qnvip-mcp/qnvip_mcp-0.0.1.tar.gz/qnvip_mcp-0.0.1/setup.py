from setuptools import setup, find_packages

setup(
    name="qnvip-mcp",
    version="0.0.1",
    author="lichaojie",
    description="青年优品mcp工具集",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-web-service",
    packages=find_packages(),
    install_requires=[
        "openpyxl",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
    # 定义命令行入口：用户安装后可直接执行 "qnvip-mcp" 命令
    entry_points={
        "console_scripts": [
            "qnvip-mcp = main:app.run",
        ]
    },
)