import os
import sys
import filecmp
from tabulate import tabulate
from collections import defaultdict

def collect_differences(dir1, dir2, ignore=None, base_path=""):
    """收集两个目录的结构差异信息"""
    dcmp = filecmp.dircmp(dir1, dir2, ignore=ignore)
    result = {
        'left_only': [],    # 仅在dir1存在的项目
        'right_only': [],   # 仅在dir2存在的项目
        'funny_files': [],  # 类型不一致的项目
        'common': [],       # 公共项目
        'subdirs': {}       # 子目录的差异信息
    }
    
    # 收集当前目录的差异
    current_path = base_path if base_path else "."
    
    for item in dcmp.left_only:
        result['left_only'].append(os.path.join(current_path, item))
    
    for item in dcmp.right_only:
        result['right_only'].append(os.path.join(current_path, item))
    
    for item in dcmp.funny_files:
        result['funny_files'].append(os.path.join(current_path, item))
    
    # 收集公共项目
    for item in dcmp.common:
        result['common'].append(os.path.join(current_path, item))
    
    # 递归处理子目录
    for subdir in dcmp.common_dirs:
        sub_path = os.path.join(base_path, subdir) if base_path else subdir
        result['subdirs'][subdir] = collect_differences(
            os.path.join(dir1, subdir),
            os.path.join(dir2, subdir),
            ignore=ignore,
            base_path=sub_path
        )
    
    return result

def print_table(left_items, common_items, right_items, dir1, dir2, title=None):
    """使用tabulate以三列表格形式打印项目"""
    if title:
        print(f"\n\033[1;34m{title}\033[0m")
    
    # 准备表格数据，确保行数一致
    max_rows = max(len(left_items), len(common_items), len(right_items))
    table_data = []
    
    for i in range(max_rows):
        left = left_items[i] if i < len(left_items) else ""
        common = common_items[i] if i < len(common_items) else ""
        right = right_items[i] if i < len(right_items) else ""
        
        # 为不同类型的项目添加颜色
        left_str = f"\033[1;31m{left}\033[0m"
        right_str = f"\033[1;32m{right}\033[0m"
        
        table_data.append([left_str, common, right_str])
    
    # 使用tabulate生成表格
    headers = [dir1, "公共项目", dir2]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def print_differences(diff_info, dir1, dir2, parent_dir=""):
    """递归打印收集到的差异信息"""
    # 准备当前目录的项目列表
    left_items = diff_info['left_only']
    common_items = diff_info['common']
    right_items = diff_info['right_only']
    
    # 打印当前目录的表格
    if parent_dir:
        title = f"目录: {parent_dir}"
    else:
        title = "根目录"
    
    print_table(left_items, common_items, right_items, dir1, dir2, title)
    
    # 打印类型不一致的项目
    if diff_info['funny_files']:
        print(f"\n\033[1;33m类型不一致（文件/目录冲突）:\033[0m")
        for item in diff_info['funny_files']:
            print(f"  - {item}")
    
    # 递归处理子目录
    for subdir, sub_diff in diff_info['subdirs'].items():
        subdir_path = os.path.join(parent_dir, subdir) if parent_dir else subdir
        print_differences(sub_diff, dir1, dir2, subdir_path)

def has_differences(diff_info):
    """检查是否有差异"""
    if diff_info['left_only'] or diff_info['right_only'] or diff_info['funny_files']:
        return True
    
    for sub_diff in diff_info['subdirs'].values():
        if has_differences(sub_diff):
            return True
    
    return False

def main():
    """CLI entry point for simdirdiff tool"""
    # check command line arguments
    if len(sys.argv) != 3:
        print(f"\033[1;31m用法错误！\033[0m 正确用法：")
        print(f"  simdirdiff <目录1路径> <目录2路径>")
        print(f"示例：")
        print(f"  simdirdiff ./TensorRT-dir1 ./TensorRT-dir2")
        sys.exit(1)
    
    # get directory paths from command line
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    
    # validate directories exist and are valid
    if not os.path.exists(dir1):
        print(f"\033[1;31m错误：\033[0m 目录 '{dir1}' 不存在")
        sys.exit(1)
    if not os.path.isdir(dir1):
        print(f"\033[1;31m错误：\033[0m '{dir1}' 不是一个有效目录")
        sys.exit(1)
    if not os.path.exists(dir2):
        print(f"\033[1;31m错误：\033[0m 目录 '{dir2}' 不存在")
        sys.exit(1)
    if not os.path.isdir(dir2):
        print(f"\033[1;31m错误：\033[0m '{dir2}' 不是一个有效目录")
        sys.exit(1)
    
    # ignore list for common files/directories
    ignore_list = [
        ".git",          # ignore git directory
        "*.log",         # ignore all .log files
        "tmp",           # ignore tmp directory
        "__pycache__"    # ignore Python cache directory
    ]
    
    # start comparison
    print(f"\033[1;34m=== 开始对比目录结构 ===\033[0m")
    diff_info = collect_differences(dir1, dir2, ignore=ignore_list)
    
    # print results
    print_differences(diff_info, dir1, dir2)
    
    # final summary
    if has_differences(diff_info):
        print(f"\n\033[1;31m=== 对比完成：两个目录结构存在差异 ===\033[0m")
        sys.exit(1)  # exit code 1 when differences found
    else:
        print(f"\n\033[1;32m=== 对比完成：两个目录结构完全一致 ===\033[0m")
        sys.exit(0)  # exit code 0 when no differences


if __name__ == "__main__":
    main()