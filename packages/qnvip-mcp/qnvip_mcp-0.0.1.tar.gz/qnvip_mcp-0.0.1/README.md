# 青年优品mcp工具集

## 支持功能
1. markdown的table 转 excel `python util/md2excel.py xxx.md xxx.xlsx` 



## 包构建发布命令
1. 安装打包工具
pip install setuptools twine

2. 构建包
python setup.py sdist bdist_wheel

3.  上传到 PyPI（需先注册账号）
twine upload dist/*


## 如何使用

# 安装你的服务
pip install qnvip-tools-sets-mcp

# 启动服务（通过你定义的命令）
qnvip-mcp