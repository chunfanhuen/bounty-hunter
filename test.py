from bs4 import BeautifulSoup
from urllib.parse import urljoin
import openpyxl
import requests
import chardet

base_url = "https://www.gdmu.edu.cn/"
page_url_pattern = "https://www.gdmu.edu.cn/xxyw1/{}.htm"
start_page = 44
end_page = 50

news_data = []

# 遍历页面
for page_num in range(start_page, end_page + 1):
    url = page_url_pattern.format(page_num)

    try:
        # 发送请求并获取网页内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 自动检测编码
        detected_encoding = chardet.detect(response.content)['encoding']
        response.encoding = detected_encoding

        html_content = response.text

        # 解析网页内容
        soup = BeautifulSoup(html_content, 'html.parser')

        news_list = soup.find('ul', class_='news_list')
        news_items = news_list.find_all('li')

        for item in news_items:
            title = item.find('a').get('title')
            date = item.find('span').text
            link = item.find('a').get('href')
            full_link = urljoin(base_url, link)

            # 过滤日期
            if "2024" in date and ("01" in date or "02" in date or "03" in date or "04" in date or "05" in date):
                news_data.append({'title': title, 'date': date, 'link': full_link})

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while processing {url}: {e}")

# 处理不包含具体页面编号的首页 URL (这个是从六月到现在的数据，如果不需要可以删除 不影响运行)
home_url = "https://www.gdmu.edu.cn/xxyw1.htm"
try:
    response = requests.get(home_url)
    response.raise_for_status()

    detected_encoding = chardet.detect(response.content)['encoding']
    response.encoding = detected_encoding

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    news_list = soup.find('ul', class_='news_list')
    news_items = news_list.find_all('li')

    for item in news_items:
        title = item.find('a').get('title')
        date = item.find('span').text
        link = item.find('a').get('href')
        full_link = urljoin(base_url, link)

        if "2024" in date and ("01" in date or "02" in date or "03" in date or "04" in date or "05" in date):
            news_data.append({'title': title, 'date': date, 'link': full_link})

except requests.exceptions.RequestException as e:
    print(f"Error occurred while processing {home_url}: {e}")

# 写入excel文件
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "News Data"
ws.append(['Date', 'Title', 'Link'])

for news in news_data:
    ws.append([news['date'], news['title'], news['link']])
wb.save("news_data.xlsx")

for news in news_data:
    print(f"Title: {news['title']}, Date: {news['date']}, Link: {news['link']}")
