from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

url = "https://www.twse.com.tw/zh/ETFortune/dividendList?stkNo=&startDate=2023&endDate=2023"
url = "https://www.wantgoo.com/stock/etf/dividend/2023"
# 啟動瀏覽器並訪問網站
driver = webdriver.Chrome()  # 或者您可以使用其他的瀏覽器，例如Chrome
driver.get(url)

# 等待表格的資料被載入
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

# 模擬滾動頁面以載入所有的資料
for _ in range(500):  # 這個數字可能需要調整，以確保載入所有的資料
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.1)  # 等待資料被載入

# 抓取表格的資料
html = driver.page_source
df = pd.read_html(html)[0]

print(df)

driver.quit()

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.twse.com.tw/zh/ETFortune/dividendList?stkNo=&startDate=2023&endDate=2023"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')  # 找到網頁中的表格
df = pd.read_html(str(table))[0]  # 將表格轉換為pandas DataFrame

print(df)

import requests
import pandas as pd

url = 'https://www.wantgoo.com/stock/etf/dividend/2023'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
tables = pd.read_html(response.text)

# `tables` 是一個包含所有表格數據的列表，每個表格都是一個 DataFrame 對象。
# 例如，如果你想查看第一個表格，你可以使用 `tables[0]`：
print(tables[0])

import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# 设置 Selenium webdriver
s = Service(ChromeDriverManager().install())

# 随机化请求头信息
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # 添加更多 User-Agent
]

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents)}")
driver = webdriver.Chrome(service=s, options=options)

url = 'https://www.wantgoo.com/stock/etf/dividend/2023/'
driver.get(url)

# 等待页面加载完成
time.sleep(random.randint(5, 10))

# 获取页面源码并用 BeautifulSoup 解析
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 寻找活跃的 tab-pane
tab_pane = soup.find('div', {'class': 'tab-pane fade show active'})

# 寻找活跃 tab-pane 中的表格
table = tab_pane.find('table')

# 寻找表格中的 tbody
tbody = table.find('tbody')

# 寻找 tbody 中的所有行（tr 元素）
rows = tbody.find_all('tr')

data = []
for row in rows:
    # 寻找每行中的所有列（td 元素）
    cols = row.find_all('td')
    # 提取每列的文本并删除首尾空白
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)

# 从提取的数据创建 DataFrame
df = pd.DataFrame(data)

print(df)

# 关闭驱动程序
driver.quit()
