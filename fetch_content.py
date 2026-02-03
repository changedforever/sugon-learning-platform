import requests
from bs4 import BeautifulSoup

url = "https://support.huawei.com/enterprise/zh/knowledge/EKB1000124709"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 找到正文内容区域
    content_div = soup.find('div', class_='col-md-9')
    if not content_div:
        content_div = soup.find('div', class_='knowledge-content')
    if not content_div:
        content_div = soup.find('main')
    
    if content_div:
        # 移除侧边栏相关内容
        sidebar = content_div.find('div', class_='sidebar')
        if sidebar:
            sidebar.decompose()
        
        # 提取正文内容
        content = content_div.prettify()
        print(content)
    else:
        print("未找到正文内容")
        # 打印整个页面结构以便分析
        print(soup.prettify())
except Exception as e:
    print(f"获取网页内容失败: {e}")
