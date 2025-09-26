import os
from PySide2.QtWidgets import QApplication
from tessng import TessngFactory
from MyPlugin import MyPlugin


if __name__ == "__main__":
    # 创建工作空间文件夹
    workspace_dir_path: str = os.path.join(os.getcwd(), "WorkSpace")
    os.makedirs(workspace_dir_path, exist_ok=True)

    # 构建配置
    config = {
        "__netfilepath": "",                # TODO 路网文件路径
        "__workspace": "D:/TESSNG/V4.0.20",  # 工作空间路径
        "__simuafterload": True,            # 加载路网后是否自动开启仿真
        "__custsimubysteps": False,         # 是否自定义仿真函数调用频率
    }

    # 创建 Qt 应用程序实例
    app = QApplication()
    # 创建自定义插件类实例
    my_plugin = MyPlugin()
    # 创建 TESS NG 工厂类实例
    factory = TessngFactory()
    # 通过工厂类构建 TESS NG 仿真核心对象
    tessng = factory.build(my_plugin, config)
    # 判断仿真核心对象是否创建成功
    if tessng is not None:
        # 启动 Qt 应用程序的事件循环，进入事件循环后，程序会持续响应用户操作和仿真事件
        app.exec_()
