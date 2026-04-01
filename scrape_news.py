#!/usr/bin/env python3
"""
News Scraper - 获取纽约时报和 AOL 的最新新闻
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json

def get_nyt_news():
    """获取纽约时报最新新闻"""
    url = "https://www.nytimes.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        news_items = []
        # 查找新闻标题和链接
        articles = soup.find_all('article')[:20]  # 限制前20条

        for article in articles:
            title_tag = article.find(['h3', 'h2', 'h4'])
            link_tag = article.find('a', href=True)

            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']

                # 处理相对链接
                if link.startswith('/'):
                    link = url + link

                if title and link:
                    news_items.append({
                        'source': 'New York Times',
                        'title': title,
                        'link': link,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })

        return news_items

    except Exception as e:
        print(f"Error fetching NYT news: {e}")
        return []

def get_aol_news():
    """获取 AOL 最新新闻"""
    url = "https://www.aol.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        news_items = []
        # 查找新闻标题和链接
        articles = soup.find_all('article')[:20]  # 限制前20条

        for article in articles:
            title_tag = article.find(['h3', 'h2', 'h4'])
            link_tag = article.find('a', href=True)

            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']

                # 处理相对链接
                if link.startswith('/'):
                    link = url + link

                if title and link:
                    news_items.append({
                        'source': 'AOL',
                        'title': title,
                        'link': link,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })

        return news_items

    except Exception as e:
        print(f"Error fetching AOL news: {e}")
        return []

def main():
    print("开始抓取新闻...")

    # 获取新闻
    nyt_news = get_nyt_news()
    aol_news = get_aol_news()

    # 合并新闻
    all_news = nyt_news + aol_news

    print(f"共获取 {len(all_news)} 条新闻")
    print(f"纽约时报: {len(nyt_news)} 条")
    print(f"AOL: {len(aol_news)} 条")

    # 创建 DataFrame
    df = pd.DataFrame(all_news)

    # 生成文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    excel_file = f'news_list_{timestamp}.xlsx'

    # 保存到 Excel
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Excel 文件已生成: {excel_file}")

    # 输出 JSON 格式（用于 GitHub Actions）
    output = {
        'total': len(all_news),
        'nyt_count': len(nyt_news),
        'aol_count': len(aol_news),
        'excel_file': excel_file,
        'news': all_news
    }

    with open('news_output.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("新闻抓取完成！")

if __name__ == '__main__':
    main()
