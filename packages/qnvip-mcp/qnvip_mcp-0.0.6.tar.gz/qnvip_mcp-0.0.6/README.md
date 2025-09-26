# 青年优品mcp工具集

## 支持功能
1. markdown的table 转 excel `python util/md2excel.py xxx.md xxx.xlsx` 

## 如何使用

### 方式1: 直接安装使用
```bash
# 安装你的服务
pip install -i https://pypi.org/simple/  -U qnvip-mcp

# 启动服务（通过你定义的命令）
qnvip-mcp
```

### 方式2: 使用 uv run（推荐）
```bash
# 直接运行，无需安装（需要先上传到 PyPI）
uv run --with qnvip-mcp -U qnvip-mcp

# 或者指定 PyPI 源
uv run --with qnvip-mcp -U qnvip-mcp  --index-url https://pypi.org/simple/ qnvip-mcp
```

### 方式3: 在项目中使用
```bash
# 添加到项目依赖
uv add qnvip-mcp

# 运行
uv run qnvip-mcp
```

## 发布说明
详细的包构建发布命令请参考：[PUBLISH.md](PUBLISH.md)

