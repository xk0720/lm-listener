import os
import time
import yaml
import torch


class DebugConfig:
    """调试配置管理类

    这个类负责从YAML文件加载调试配置，并提供统一的调试信息打印接口。
    它使用单模例式确保同在整个程序中使用相的配置。
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DebugConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """初始化配置类，只在第一次创建实例时执行"""
        if self._initialized:
            return

        # 加载YAML配置文件
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'configs',
            'debug_config.yaml'
        )

        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # 设置调试标志
        self.DEBUG = config['debug']
        self.DEBUG_INIT = config['debug_flags']['init']
        self.DEBUG_DATA = config['debug_flags']['data']
        self.DEBUG_MODEL = config['debug_flags']['model']
        self.DEBUG_DIST = config['debug_flags']['dist']

        # 设置格式选项
        # self.show_time = config['debug_format']['show_time']
        # self.show_rank = config['debug_format']['show_rank']
        # self.show_gpu = config['debug_format']['show_gpu']

        self._initialized = True

    # def debug_print(self, flag, message):
    #     """统一的调试信息打印函数
    #
    #     Args:
    #         flag: 调试类型标志（如 DEBUG_INIT）
    #         message: 要打印的信息
    #     """
    #     if not self.DEBUG or not flag:
    #         return
    #
    #     parts = []
    #
    #     # 添加时间戳
    #     if self.show_time:
    #         time_str = time.strftime("%H:%M:%S")
    #         parts.append(f"[{time_str}]")
    #
    #     # 添加进程rank信息
    #     if self.show_rank:
    #         rank = int(os.environ.get("RANK", "0"))
    #         parts.append(f"[Rank {rank}]")
    #
    #     # 添加GPU信息
    #     if self.show_gpu and torch.cuda.is_available():
    #         gpu_id = torch.cuda.current_device()
    #         parts.append(f"[GPU {gpu_id}]")
    #
    #     # 组合完整的调试信息
    #     debug_message = " ".join(parts + [str(message)])
    #     print(debug_message)


# 创建全局配置实例
debug_config = DebugConfig()
