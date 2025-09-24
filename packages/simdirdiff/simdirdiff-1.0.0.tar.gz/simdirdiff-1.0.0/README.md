# simdirdiff

一个简单的目录结构比较工具，使用 uv 进行包管理。

## 安装

使用 uv 安装：

```bash
cd dir_diff
uv sync
```

## 使用方法

```bash
# 使用 uv 运行
uv run simdirdiff <目录1路径> <目录2路径>

# 或者安装后直接使用
simdirdiff <目录1路径> <目录2路径>
```

## 示例

```bash
uv run simdirdiff ./TensorRT-dir1 ./TensorRT-dir2
```

## 功能

- 比较两个目录的结构差异
- 以表格形式显示差异
- 支持颜色输出
- 自动忽略常见文件（.git, *.log, tmp, __pycache__）
- 递归比较子目录
- 返回适当的退出码（0=无差异，1=有差异）