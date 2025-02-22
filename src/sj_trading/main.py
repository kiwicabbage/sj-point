# main.py
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread
from .ui import TradingMonitor
import sys
from .logic.Backend import BackendWorker





if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 啟動 UI
    window = TradingMonitor([], [], [], [])
    # 後端工作使用 QThread
    backend_thread = QThread()
    backend_worker = BackendWorker()
    backend_worker.moveToThread(backend_thread)

    # 按鈕與後端下單邏輯連接
    backend_worker.data_ready.connect(window.update_all_tables)

    window.place_order_signal.connect(backend_worker.firstOrderBottom)
    # QTimer 啟動於正確的執行緒中
    backend_thread.started.connect(backend_worker.timer.start)
    backend_thread.started.connect(backend_worker.respond_timer.start)
    backend_thread.start()
    backend_worker.update_data()

    sys.exit(app.exec())



