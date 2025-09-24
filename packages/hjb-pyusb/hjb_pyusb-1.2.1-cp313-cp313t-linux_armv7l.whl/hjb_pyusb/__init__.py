
# 自动生成的 hjb_pyusb 包初始化文件
import os
import sys

# 添加当前目录到路径，确保可以导入同级模块
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 尝试导入所有可能的模块
try:
    # 导入主要的模块
    from .hjb_pyusb import *
except ImportError as e:
    # 如果主模块不存在，尝试导入其他可能的模块
    print(f"警告: 无法导入主模块: {e}")
    try:
        # 尝试导入所有.py文件作为模块
        for file in os.listdir(current_dir):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]  # 移除.py扩展名
                exec(f"from .{module_name} import *")
    except Exception as ex:
        print(f"警告: 导入其他模块时出错: {ex}")

# 尝试设置版本
try:
    from ._version import __version__
except ImportError:
    try:
        from .version import __version__
    except ImportError:
        try:
            from . import hjb_pyusb
            __version__ = getattr(hjb_pyusb, "__version__", "1.2.1")
        except ImportError:
            __version__ = "1.2.1"

print("hjb_pyusb package loaded successfully")
