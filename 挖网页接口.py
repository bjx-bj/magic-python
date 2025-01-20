import requests
from bs4 import BeautifulSoup
import re

def extract_api_links(url):
    # 发送请求获取网页内容
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch webpage. Status code {response.status_code}")
        return []
    
    # 使用 BeautifulSoup 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取所有的链接
    links = soup.find_all('a', href=True)
    
    # 使用正则表达式检查链接中是否包含 API 的相关标志
    api_links = []
    for link in links:
        href = link['href']
        
        # 检查是否包含 ".json"、".api" 或 "api" 关键字
        if re.search(r'(api|\.json|\.api)', href, re.IGNORECASE):
            api_links.append(href)
    
    return api_links

# 示例使用
url = 'https://example.com'  # 替换为你要分析的网页 URL
api_links = extract_api_links(url)

if api_links:
    print("Found API links:")
    for api in api_links:
        print(api)
else:
    print("No API links found.")
