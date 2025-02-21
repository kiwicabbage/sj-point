# ui.py
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont, QMovie
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QSize
from .tradingTime import is_trading_hours

class TradingMonitor(QWidget):
    place_order_signal = pyqtSignal()
    
    def __init__(self, sugCall, sugPut, posCall, posPut):
        super().__init__()
        self.sugCall = sugCall
        self.sugPut = sugPut
        self.posCall = posCall
        self.posPut = posPut
        self.counter = 60
        self.setGeometry(150, 150, 600, 600)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.trading_hour_label = QLabel()
        self.trading_hour_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.trading_hour_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_trading_status()
        # self.trading_hour_label = QLabel("Not Trading Hour!")
        # self.trading_hour_label.setStyleSheet("color: red;")
            

        self.timer_label = QLabel(f"Time remaining: {self.counter}s")
        self.timer_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        timer_layout = QHBoxLayout()
        timer_layout.addWidget(self.trading_hour_label)
        timer_layout.addWidget(self.timer_label)
        layout.addLayout(timer_layout)
        

        # ✅ GIF 動畫
        self.gif_label = QLabel()
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        gif_path = "/Users/superstone/code/pycode/SJ_trading_system/sj-trading/src/sj_trading/pokemon-pokémon.gif"  # ⬅️ 請更換為你的 GIF 路徑
        self.movie = QMovie(gif_path)
        self.movie.setScaledSize(QSize(200, 200))  # 💡 調整這裡以更改大小
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(self.gif_label)

        # 合約表格
        self.current_contract_layout, self.current_contract_table = self.create_contract_table("Current Contract")
        layout.addLayout(self.current_contract_layout)

        self.suggested_contract_layout, self.suggested_contract_table = self.create_contract_table("Suggested Contract")
        layout.addLayout(self.suggested_contract_layout)

        # 設定下單按鈕
        set_order_button = QPushButton("Set First Order")
        set_order_button.setFont(QFont("Arial", 12))
        set_order_button.clicked.connect(lambda: self.place_order_signal.emit())
        layout.addWidget(set_order_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle("Trading System Monitor (Point Method)")
        self.show()

    def update_trading_status(self):
        if is_trading_hours():  # 確保這是函式呼叫
            self.trading_hour_label.setText("🟢 Trading Hour!")
            self.trading_hour_label.setStyleSheet("color: green; background-color: #E8F5E9;")
        else:
            self.trading_hour_label.setText("🔴 Not Trading Hour!")
            self.trading_hour_label.setStyleSheet("color: red; background-color: #FFEBEE;")
            
    def create_contract_table(self, title):
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title_label.setStyleSheet("background-color: #4A90E2; color: white; padding: 5px; border-radius: 5px;")
        layout.addWidget(title_label)

        table = QTableWidget(2, 5)
        table.setHorizontalHeaderLabels(["Strike Price", "Price", "Bid", "Ask", "UR PnL"])
        table.setVerticalHeaderLabels(["Call", "Put"])
        table.setStyleSheet("QHeaderView::section { background-color: #2C3E50; color: white; font-weight: bold; padding: 4px; }")
        layout.addWidget(table)

        return layout, table  # ⚡️ 回傳 table

    def update_timer(self):
        self.update_trading_status()
        if self.counter > 0:
            self.counter -= 1
            self.timer_label.setText(f"Time remaining: {self.counter}s")
        else:
            self.counter = 60
            self.timer_label.setText("Recalculating...")

    def update_all_tables(self, sugCall, sugPut, posCall, posPut):
        # print(f"✅ UI 更新表格：\nCall: {sugCall}\nPut: {sugPut}\nPosCall: {posCall}\nPosPut: {posPut}")
        self.sugCall, self.sugPut = sugCall, sugPut
        self.posCall, self.posPut = posCall, posPut
        # update position table
        self.update_contract_table(self.current_contract_table, posCall, posPut, True)
        # update suggested contract table
        self.update_contract_table(self.suggested_contract_table, sugCall, sugPut)


    def update_contract_table(self, table, call_data, put_data, Pnl = False):
        """直接使用 QTableWidget，而不是 layout"""
        # Call 資料
        if call_data:
            table.setItem(0, 0, QTableWidgetItem(str(call_data[0])[3:-2]))
            table.setItem(0, 1, QTableWidgetItem(str(call_data[1])))
            table.setItem(0, 2, QTableWidgetItem(str(call_data[2])))
            table.setItem(0, 3, QTableWidgetItem(str(call_data[3])))

        # Put 資料
        if put_data:
            table.setItem(1, 0, QTableWidgetItem(str(put_data[0])[3:-2]))
            table.setItem(1, 1, QTableWidgetItem(str(put_data[1])))
            table.setItem(1, 2, QTableWidgetItem(str(put_data[2])))
            table.setItem(1, 3, QTableWidgetItem(str(put_data[3])))
            
        if Pnl:
            table.setItem(0, 4, QTableWidgetItem(str(call_data[4])))
            table.setItem(1, 4, QTableWidgetItem(str(put_data[4])))
