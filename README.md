# News Scraper

自动抓取纽约时报和 AOL 的最新新闻，生成 Excel 文件。

## 功能

- 📰 获取纽约时报最新新闻
- 📰 获取 AOL 最新新闻
- 📊 生成 Excel 格式的新闻列表
- 🤖 GitHub Actions 自动运行

## 使用方法

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行脚本
python scrape_news.py
```

### GitHub Actions

推送代码到 GitHub 后，Actions 会自动运行：
- 每次推送时运行
- 每天自动运行（北京时间 08:00）
- 也可以手动触发

## 输出

- `news_list_YYYYMMDD_HHMMSS.xlsx` - 新闻列表 Excel 文件
- `news_output.json` - JSON 格式的新闻数据

## 依赖

- Python 3.7+
- requests
- beautifulsoup4
- pandas
- openpyxl
