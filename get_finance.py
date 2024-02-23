import matplotlib
matplotlib.use('Agg')
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# 定義股票代碼和日期範圍
ticker = "0050.TW"
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# 獲取股票數據
data = yf.download(ticker, start=start_date, end=end_date)

# 繪製股價走勢圖
plt.figure(figsize=(8, 4), dpi=150)  # 調整圖片大小和解析度
plt.plot(data['Close'])
plt.title('0050 ETF Price Over the Last Month')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)

# 調整周圍空白
plt.tight_layout()

# 保存走势图
plt.savefig('0050_price.png', bbox_inches='tight')  # 添加bbox_inches='tight'參數

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 将走势图插入Excel的最后一列
img = Image('0050_price.png')
img.width = 200  # 调整图像宽度以适应单元格大小
img.height = 100  # 调整图像高度以适应单元格大小
ws.add_image(img, f"{chr(ord('A') + ws.max_column)}1")  # 插入到最后一列

# 保存Excel文件
wb.save('output.xlsx')
