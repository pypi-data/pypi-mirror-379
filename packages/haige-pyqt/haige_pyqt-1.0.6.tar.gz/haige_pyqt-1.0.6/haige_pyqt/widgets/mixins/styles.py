from PyQt5.QtCore import Qt


class TopMostMixin:
    def set_topMost(self):
        self.setAttribute(Qt.WA_AlwaysStackOnTop, True)

    def unset_topMost(self):
        self.setAttribute(Qt.WA_AlwaysStackOnTop, False)


class CenterPosMixin:
    def move_to_center(self, ref_widget):
        if ref_widget:
            """将子窗口居中到当前窗口"""
            # 获取主窗口的中心点
            main_window_center = ref_widget.geometry().center()

            # 计算子窗口左上角应该移动到的位置
            x = main_window_center.x() - self.width() // 2
            y = main_window_center.y() - self.height() // 2

            # 移动子窗口
            self.move(x, y)
